import matplotlib.pyplot as plt
from simple_pid import PID
from wpimath.geometry import Pose2d, Rotation2d, Translation2d
from wpimath.kinematics import (
    ChassisSpeeds,
    SwerveDrive4Kinematics,
    SwerveDrive4Odometry,
)
from wpimath.trajectory import TrajectoryConfig, TrajectoryGenerator

from motion import HolonomicDriveController


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


config = TrajectoryConfig(maxVelocity=1, maxAcceleration=2)

initial_pose = Pose2d(x=0, y=0, rotation=Rotation2d(0))
waypoints = [Translation2d(x=1, y=1), Translation2d(x=2, y=-1)]
final_pose = Pose2d(x=3, y=0, rotation=Rotation2d(0))

trajectory = TrajectoryGenerator.generateTrajectory(
    start=initial_pose, interiorWaypoints=waypoints, end=final_pose, config=config
)

Kp = 10

controller = HolonomicDriveController(
    pid_x=PID(Kp=Kp, sample_time=None), pid_y=PID(Kp=Kp, sample_time=None)
)

fl_loc = Translation2d(0.3, 0.3)
fr_loc = Translation2d(0.3, -0.3)
rl_loc = Translation2d(-0.3, 0.3)
rr_loc = Translation2d(-0.3, -0.3)

kinematics = SwerveDrive4Kinematics(fl_loc, fr_loc, rl_loc, rr_loc)
odometry = SwerveDrive4Odometry(kinematics, Rotation2d(), initial_pose)

odometry_poses = []

for state in trajectory.states():
    speeds = controller.calculate(odometry.getPose(), state)

    module_states = kinematics.toSwerveModuleStates(speeds)

    odometry_poses.append(odometry.getPose())

    odometry.updateWithTime(
        state.t,
        Rotation2d(),
        module_states[0],
        module_states[1],
        module_states[2],
        module_states[3],
    )

fig, ax = plt.subplots()
ax.scatter(
    [pose.X() for pose in odometry_poses],
    [pose.Y() for pose in odometry_poses],
    label="odometry",
    marker="o",
)
ax.scatter(
    [state.pose.X() for state in trajectory.states()],
    [state.pose.Y() for state in trajectory.states()],
    label="trajectory",
    alpha=0.5,
)
ax.legend()
ax.set_title(f"HolonomicController Kp={Kp}")
ax.set_xlabel("Field X (meters)")
ax.set_ylabel("Field Y (meters)")
ax.set_aspect("equal", "box")
plt.savefig(f"Kp={Kp}.svg")
plt.show()

print(f"trajectory time = {trajectory.totalTime():0.3} sec")
print(f"translation_error_max = {controller.max_translation_error:0.3} meters")
print(
    "translation_error_max position:"
    f" x = {controller.translation_error_max_pos.x:0.3} meters,"
    f" y = {controller.translation_error_max_pos.y:0.3} meters"
)
print(f"x_fb_max = {controller.x_fb_max:0.3} meters/sec")
print(f"y_fb_max = {controller.y_fb_max:0.3} meters/sec")
