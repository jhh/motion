import math

import matplotlib.patches as patches
import matplotlib.pyplot as plt
from wpimath.geometry import Translation2d
from wpimath.kinematics import ChassisSpeeds
from wpimath.spline import QuinticHermiteSpline
from more_itertools import pairwise


def plot_swerve(wheel_locs, module_states):
    wheel_locs_x = [loc.x for loc in wheel_locs]
    wheel_locs_y = [loc.y for loc in wheel_locs]

    wheel_vecs_x = [s.speed * s.angle.cos() for s in module_states]
    wheel_vecs_y = [s.speed * s.angle.sin() for s in module_states]

    fig, ax = plt.subplots()
    rect = patches.Rectangle(
        (wheel_locs_x[3], wheel_locs_y[3]),
        wheel_locs_x[0] - wheel_locs_x[3],
        wheel_locs_y[0] - wheel_locs_y[3],
        linewidth=1,
        edgecolor="r",
        facecolor="none",
    )
    ax.add_patch(rect)

    plt.quiver(
        wheel_locs_x,
        wheel_locs_y,
        wheel_vecs_x,
        wheel_vecs_y,
        angles="xy",
        scale_units="xy",
        scale=2,
        width=0.0125,
    )

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    offset = -0.12
    plt.text(wheel_locs_x[0] + offset, wheel_locs_y[0] + offset, "FL")
    plt.text(wheel_locs_x[1] + offset, wheel_locs_y[1] + offset, "FR")
    plt.text(wheel_locs_x[2] + offset, wheel_locs_y[2] + offset, "RL")
    plt.text(wheel_locs_x[3] + offset, wheel_locs_y[3] + offset, "RR")
    ax.set_aspect("equal", "box")
    plt.savefig("swerve.svg")
    plt.show()


def plot_trajectories(
    holonomic_speeds, odometry_poses, trajectory_states, Kp, arrows=False
):
    fig, ax = plt.subplots()
    ax.scatter(
        [pose.X() for pose in odometry_poses],
        [pose.Y() for pose in odometry_poses],
        label="odometry",
    )
    ax.scatter(
        [state.pose.X() for state in trajectory_states],
        [state.pose.Y() for state in trajectory_states],
        label="trajectory",
        alpha=0.5,
    )

    if arrows:
        sampled_odometry_poses = []
        sampled_holonomic_speeds = []
        for i in range(0, len(odometry_poses), 8):
            sampled_odometry_poses.append(odometry_poses[i])
            sampled_holonomic_speeds.append(holonomic_speeds[i])
        ax.quiver(
            [pose.X() for pose in sampled_odometry_poses],
            [pose.Y() for pose in sampled_odometry_poses],
            [s.vx for s in sampled_holonomic_speeds],
            [s.vy for s in sampled_holonomic_speeds],
            angles="xy",
            scale_units="xy",
            scale=2,
            color="r"
            # width=0.0125,
        )

    ax.legend()
    ax.set_title(f"HolonomicDriveController Kp={Kp}")
    ax.set_xlabel("Field X (meters)")
    ax.set_ylabel("Field Y (meters)")
    ax.set_aspect("equal", "box")
    plt.savefig(f"Kp={Kp}.svg")
    plt.show()


def plot_splines(
    ax=None,
    waypoints=None,
    xlim=None,
    ylim=None,
    show_vectors=True,
):
    if ax is None:
        _, ax = plt.subplots()

    ax.set_aspect("equal", "box")

    if not xlim is None:
        ax.set_xlim(*xlim)
    if not ylim is None:
        ax.set_ylim(*ylim)

    if show_vectors:
        ax.quiver(
            [wp[0][0] for wp in waypoints],
            [wp[0][1] for wp in waypoints],
            [wp[1][0] for wp in waypoints],
            [wp[1][1] for wp in waypoints],
            angles="xy",
            scale_units="xy",
            scale=2,
        )

    colors = ["b", "g", "r"]

    splines = []

    for i, (wp_start, wp_end) in enumerate(pairwise(waypoints)):
        x_init_control_vec = (wp_start[0][0], wp_start[1][0], 0)
        x_fin_control_vec = (wp_end[0][0], wp_end[1][0], 0)
        y_init_control_vec = (wp_start[0][1], wp_start[1][1], 0)
        y_fin_control_vec = (wp_end[0][1], wp_end[1][1], 0)

        spline = QuinticHermiteSpline(
            x_init_control_vec, x_fin_control_vec, y_init_control_vec, y_fin_control_vec
        )

        splines.append(spline)

        points_x = []
        points_y = []

        for j in range(0, 50):
            t = j / 50
            pose, _ = spline.getPoint(t)
            points_x.append(pose.X())
            points_y.append(pose.Y())

        ax.plot(points_x, points_y, color=colors[i % 3], label=f"spline {i+1}")

    ax.legend()
    return ax, splines


class HolonomicDriveController:
    def __init__(self, pid_x, pid_y):
        self.pid_x = pid_x
        self.pid_y = pid_y
        self.max_translation_error = 0
        self.max_translation_error_max_pos = Translation2d()
        self.x_fb_max = 0
        self.y_fb_max = 0

    def calculate(self, current_pose, desired_state):
        pose_ref = desired_state.pose
        velocity_ref = desired_state.velocity

        x_ff = velocity_ref * pose_ref.rotation().cos()
        y_ff = velocity_ref * pose_ref.rotation().sin()
        theta_ff = 0

        self.pid_x.setpoint = pose_ref.X()
        self.pid_y.setpoint = pose_ref.Y()
        x_fb = self.pid_x(current_pose.X())
        y_fb = self.pid_y(current_pose.Y())

        # log max error and feedback correction
        translation_error = pose_ref.translation().distance(current_pose.translation())
        if translation_error > self.max_translation_error:
            self.max_translation_error = translation_error
            self.translation_error_max_pos = current_pose.translation()

        if abs(x_fb) > abs(self.x_fb_max):
            self.x_fb_max = x_fb

        if abs(y_fb) > abs(self.y_fb_max):
            self.y_fb_max = y_fb

        return ChassisSpeeds(x_ff + x_fb, y_ff + y_fb, theta_ff)
