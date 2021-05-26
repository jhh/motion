import json
import math
from functools import cached_property
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


class Measure:
    def __init__(self, id, description):
        self.id = id
        self.description = description

    @classmethod
    def from_json(cls, measure):
        return Measure(id=measure["id"], description=measure["description"])

    def __repr__(self):
        return f"Measure(id={self.id!r},description={self.description!r})"

    def __eq__(self, o: object):
        return self.id == o.id

    def __hash__(self):
        return id.__hash__()


Measure.HC_VX = Measure(id="HC Vx", description="HC Vx")
Measure.HC_VY = Measure(id="HC Vy", description="HC Vy")
Measure.HC_OMEGA = Measure(id="HC Omega", description="HC Omega")
Measure.TRAJECTORY_VELOCITY = Measure(id="Traj. Vel", description="Traj. Vel")
Measure.TRAJECTORY_X = Measure(id="Traj. X", description="Traj. X")
Measure.TRAJECTORY_Y = Measure(id="Traj. Y", description="Traj. Y")
Measure.GYRO_ANGLE_DEGREE = Measure(
    id="Gyro Angle (deg)", description="Gyro Angle (deg)"
)
Measure.ODOMETRY_X = Measure(id="Odometry X", description="Odometry X")
Measure.ODOMETRY_Y = Measure(id="Odometry Y", description="Odometry Y")
Measure.GYRO_ROTATION2D_DEGREE = Measure(
    id="Gyro Rotation2d (deg)", description="Gyro Rotation2d (deg)"
)
Measure.OUTPUT_PERCENT = Measure(id="OUTPUT_PERCENT", description="Output Percentage")
Measure.QUAD_B_PIN = Measure(id="QUAD_B_PIN", description="Quad B Pin State")
Measure.QUAD_IDX_PIN = Measure(id="QUAD_IDX_PIN", description="Quad Index Pin State")
Measure.QUAD_POSITION = Measure(id="QUAD_POSITION", description="Quad Position")
Measure.QUAD_VELOCITY = Measure(id="QUAD_VELOCITY", description="Quad Velocity")
Measure.PULSE_WIDTH_POSITION = Measure(
    id="PULSE_WIDTH_POSITION", description="Pulse Width Position"
)
Measure.PULSE_WIDTH_VELOCITY = Measure(
    id="PULSE_WIDTH_VELOCITY", description="Pulse Width Velocity"
)
Measure.PULSE_WIDTH_RISE_TO_FALL = Measure(
    id="PULSE_WIDTH_RISE_TO_FALL", description="PWM Pulse Width"
)
Measure.PULSE_WIDTH_RISE_TO_RISE = Measure(
    id="PULSE_WIDTH_RISE_TO_RISE", description="PWM Period"
)
Measure.FORWARD_LIMIT_SWITCH_CLOSED = Measure(
    id="FORWARD_LIMIT_SWITCH_CLOSED", description="Forward Limit Switch Closed"
)
Measure.REVERSE_LIMIT_SWITCH_CLOSED = Measure(
    id="REVERSE_LIMIT_SWITCH_CLOSED", description="Reverse Limit Switch Closed"
)
Measure.TEMPERATURE = Measure(id="TEMPERATURE", description="Controller Temperature")
Measure.INTEGRATED_SENSOR_POSITION = Measure(
    id="INTEGRATED_SENSOR_POSITION", description="Integrated Sensor Position"
)
Measure.INTEGRATED_SENSOR_ABSOLUTE_POSITION = Measure(
    id="INTEGRATED_SENSOR_ABSOLUTE_POSITION",
    description="Integrated Sensor Abs. Position",
)
Measure.INTEGRATED_SENSOR_VELOCITY = Measure(
    id="INTEGRATED_SENSOR_VELOCITY", description="Integrated Sensor Velocity"
)
Measure.ACTIVE_TRAJECTORY_ARB_FEED_FWD = Measure(
    id="ACTIVE_TRAJECTORY_ARB_FEED_FWD", description="Active Trajectory Arb. Feed FWD"
)
Measure.SELECTED_SENSOR_POSITION = Measure(
    id="SELECTED_SENSOR_POSITION", description="Selected Sensor Position (PID 0)"
)
Measure.SELECTED_SENSOR_VELOCITY = Measure(
    id="SELECTED_SENSOR_VELOCITY", description="Selected Sensor Velocity (PID 0)"
)
Measure.ACTIVE_TRAJECTORY_POSITION = Measure(
    id="ACTIVE_TRAJECTORY_POSITION", description="Active Trajectory Position"
)
Measure.ACTIVE_TRAJECTORY_VELOCITY = Measure(
    id="ACTIVE_TRAJECTORY_VELOCITY", description="Active Trajectory Velocity"
)
Measure.CLOSED_LOOP_ERROR = Measure(
    id="CLOSED_LOOP_ERROR", description="Closed Loop Error (PID 0)"
)
Measure.BUS_VOLTAGE = Measure(id="BUS_VOLTAGE", description="Bus Voltage")
Measure.ERROR_DERIVATIVE = Measure(
    id="ERROR_DERIVATIVE", description="Error Derivative (PID 0)"
)
Measure.INTEGRAL_ACCUMULATOR = Measure(
    id="INTEGRAL_ACCUMULATOR", description="Integral Accumulator (PID 0)"
)
Measure.ANALOG_IN = Measure(id="ANALOG_IN", description="Analog Position Input")
Measure.ANALOG_IN_RAW = Measure(id="ANALOG_IN_RAW", description="Analog Raw Input")
Measure.ODOMETRY_ROTATION2D_DEGREE = Measure(
    id="Odometry Rotation2d (deg)", description="Odometry Rotation2d (deg)"
)
Measure.CLOSED_LOOP_TARGET = Measure(
    id="CLOSED_LOOP_TARGET", description="Closed-loop Setpoint (PID 0)"
)
Measure.STATOR_CURRENT = Measure(id="STATOR_CURRENT", description="Stator Current")
Measure.SUPPLY_CURRENT = Measure(id="SUPPLY_CURRENT", description="Supply Current")
Measure.OUTPUT_VOLTAGE = Measure(id="OUTPUT_VOLTAGE", description="Output Voltage")
Measure.TRAJECTORY_CURVATURE = Measure(
    id="Traj. Curvature", description="Traj. Curvature"
)
Measure.TRAJECTORY_DEGREES = Measure(id="Traj. Degrees", description="Traj. Degrees")
Measure.TRAJECTORY_TIME = Measure(id="Traj. Time", description="Traj. Time")
Measure.TRAJECTORY_ACCELERATION = Measure(id="Traj. Accel", description="Traj. Accel")
Measure.ANALOG_IN_VELOCITY = Measure(
    id="ANALOG_IN_VELOCITY", description="Analog Velocity Input"
)
Measure.QUAD_A_PIN = Measure(id="QUAD_A_PIN", description="Quad A Pin State")


class Measurable:
    def __init__(self, id, type, description, measures):
        self.id = id
        self.type = type
        self.description = description
        self.measures = measures

    @classmethod
    def from_json(cls, measurable, measures):
        return Measurable(
            id=measurable["id"],
            type=measurable["type"],
            description=measurable["description"],
            measures=[Measure.from_json(measure) for measure in measures],
        )

    def measure_by_id(self, id):
        return next(
            filter(
                lambda measure: measure.id == id,
                self.measures,
            ),
            None,
        )

    def __repr__(self):
        return f"Measurable(id={self.id!r},type={self.type!r},description={self.description!r},measures={self.measures!r})"


class Subscription:
    def __init__(self):
        self.subscription = list()
        with open("swerve_inventory.json") as f:
            self.inventory = json.load(f)
        self.measurables = []
        for measurable in self.inventory["items"]:
            measures = next(
                filter(
                    lambda measure: measure["deviceType"] == measurable["type"],
                    self.inventory["measures"],
                ),
                None,
            )
            self.measurables.append(
                Measurable.from_json(measurable, measures["deviceMeasures"])
            )

    def measurable_by_type(self, type):
        return next(
            filter(
                lambda item: item.type == type,
                self.measurables,
            ),
            None,
        )

    def measure_by_id(self, id):
        return next(
            filter(
                lambda item: item.id == id,
                self.measurables,
            ),
            None,
        )

    def append(self, measureableId, measureId):
        self.subscription.append({"itemId": measureableId, "measurementId": measureId})

    # def validate(self):
    #     for measure in self.subscription:
    #         measurable = telemetry.measure_by_id(measure.itemId)

    def to_json(self):
        sub_dict = {"type": "start", "subscription": self.subscription}
        return json.dumps(sub_dict, indent=2)

    def __iter__(self):
        return self.subscription.__iter__()

    def __repr__(self):
        return f"Subscription(type={self.type!r},subscription={self.subscription!r}"

class Telemetry:
    def __init__(self, csv):
        self.df = pd.read_csv(csv)


class TrajectoryTelemetry(Telemetry):
    def __init__(self, csv, **kwargs):
        super().__init__(csv)
        self.df.rename(
            columns={
                "trajectory_command__traj__x": "traj_x",
                "trajectory_command__traj__y": "traj_y",
                "trajectory_command__traj__vel": "traj_vel",
                "trajectory_command__traj__accel": "traj_accel",
                "trajectory_command__traj__degrees": "traj_deg",
                "trajectory_command__traj__time": "traj_time",
                "trajectory_command__hc_vx": "hc_vx",
                "trajectory_command__hc_vy": "hc_vy",
                "trajectory_command__hc_omega": "hc_omega",
                "drivesubsystem__odometry_x": "odom_x",
                "drivesubsystem__odometry_y": "odom_y",
                "drivesubsystem__gyro_rotation2d__deg_": "gyro_deg",
                "drivesubsystem__odometry_rotation2d__deg_": "odom_deg",
                "talonfx_10__closed_loop_setpoint__pid_0_": "t10_setpoint",
                "talonfx_11__closed_loop_setpoint__pid_0_": "t11_setpoint",
                "talonfx_12__closed_loop_setpoint__pid_0_": "t12_setpoint",
                "talonfx_13__closed_loop_setpoint__pid_0_": "t13_setpoint",
                "talonfx_10__selected_sensor_velocity": "t10_velocity",
                "talonfx_11__selected_sensor_velocity": "t11_velocity",
                "talonfx_12__selected_sensor_velocity": "t12_velocity",
                "talonfx_13__selected_sensor_velocity": "t13_velocity",
            },
            inplace=True,
        )
        self.df["talon_setpoint_avg"] = (
            self.df[["t10_setpoint", "t11_setpoint", "t12_setpoint", "t13_setpoint"]]
            .abs()
            .mean(axis=1)
        )
        self.df["talon_velocity_avg"] = (
            self.df[["t10_velocity", "t11_velocity", "t12_velocity", "t13_velocity"]]
            .abs()
            .mean(axis=1)
        )

        self.df['hc_omega'] = self.df['hc_omega'] * -1
        self.df['traj_time'] = self.df['traj_time'] * 1000 # sec to msec
        self.df['x_error'] = self.df['odom_x'] - self.df['traj_x']
        self.df['y_error'] = self.df['odom_y'] - self.df['traj_y']

        
        self.drive_cpr = kwargs.get("drive_cpr", 2048)
        self.drive_gear_ratio = kwargs.get(
            "drive_gear_ratio", (25.0 / 44.0) * (15.0 / 45.0)
        )
        self.wheel_diameter_in = kwargs.get("wheel_diameter_in", 3.0 * (508.0 / 504.0))
        self.wheel_circum_m = kwargs.get(
            "wheel_circum_m", math.pi * 0.0254 * self.wheel_diameter_in
        )

    @cached_property
    def start(self):
        rows = self.df[self.df["traj_vel"] > 0.0]
        return rows.iloc[0, 0] if not rows.empty else self.df['timestamp'].iloc[0]

    @cached_property
    def end(self):
        rows = self.df[(self.df["timestamp"] > self.start) & (self.df["traj_vel"] == 0)]
        return rows.iloc[0, 0] if not rows.empty else self.df['timestamp'].iloc[-1]

    def end_pose(self):
        return self.df[self.df['timestamp'] == self.end][['traj_x', 'traj_y', 'odom_x', 'odom_y', 'odom_deg']]

    def make_interval(self, start=None, end=None):
        if start == None:
            start = self.start

        if end == None:
            end = self.end

        return (self.df["timestamp"] >= start) & (self.df["timestamp"] <= end)

    @cached_property
    def interval(self):
        return self.make_interval()

    def plot_trajectory(self, interval=pd.Series(dtype="boolean"), ax=None):
        if interval.empty:
            interval = self.interval

        if ax == None:
            _, ax = plt.subplots()

        self.df[interval].plot(x="traj_x", y="traj_y", label="trajectory", ax=ax)
        self.df[interval].plot(x="odom_x", y="odom_y", label="odometry", ax=ax)
        ax.grid()
        ax.set_ylabel("meters")
        ax.set_xlabel("meters")

    def plot_error(self, interval=pd.Series(dtype="boolean"), ax=None):
        if interval.empty:
            interval = self.interval

        if ax == None:
            _, ax = plt.subplots()

        self.df[interval].plot(x='timestamp', y='x_error', ax=ax, label='x error')
        self.df[interval].plot(x='timestamp', y='y_error', ax=ax, label='y error')
        ax.grid()
        ax.set_ylabel("meters")
        ax.set_xlabel("milliseconds")


    def _drive_mps(self, counts_100ms):
        motor_rot_100ms = counts_100ms / self.drive_cpr
        wheel_rot_100ms = motor_rot_100ms * self.drive_gear_ratio
        meters_100ms = wheel_rot_100ms * self.wheel_circum_m
        return meters_100ms * 10

    def plot_velocity(
        self,
        interval=pd.Series(dtype="boolean"),
        ax=None,
        trajectory=True,
        controller=True,
        setpoint=True,
        drive=True,
    ):
        if interval.empty:
            interval = self.interval

        if ax == None:
            _, ax = plt.subplots()

        if trajectory:
            self.df[interval].plot(
                x="timestamp", y="traj_vel", ax=ax, label="trajectory"
            )

        if controller:
            hc_vel = np.hypot(self.df[interval]["hc_vx"], self.df[interval]["hc_vy"])
            ax.plot(
                self.df[interval]["timestamp"],
                hc_vel,
                label="holonomic controller",
                color="orange",
            )

        if setpoint:
            setpoint_mps = self.df["talon_setpoint_avg"].apply(self._drive_mps)
            linestyle = ":" if controller else "-"
            ax.plot(
                self.df[interval]["timestamp"],
                setpoint_mps[interval],
                label="talon setpoint",
                color="green",
                linestyle=linestyle,
            )

        if drive:
            drive_mps = self.df["talon_velocity_avg"].apply(self._drive_mps)
            # linestyle = "-" if controller else "-"
            ax.plot(
                self.df[interval]["timestamp"],
                drive_mps[interval],
                label="talon velocity",
                color="purple",
                linestyle=linestyle,
            )

        if controller and trajectory:
            ax.fill_between(
                self.df[interval]["timestamp"],
                self.df[interval]["traj_vel"],
                hc_vel,
                color="orange",
                alpha=0.2,
            )

        if setpoint and controller:
            ax.fill_between(
                self.df[interval]["timestamp"],
                setpoint_mps[interval],
                hc_vel,
                color="green",
                alpha=0.1,
            )

        if setpoint and drive:
            ax.fill_between(
                self.df[interval]["timestamp"],
                drive_mps[interval],
                setpoint_mps[interval],
                color="purple",
                alpha=0.1,
            )


        ax.legend()
        ax.grid()
        ax.set_ylabel("meters/second")
        ax.set_xlabel("milliseconds")

    def plot_yaw(self, interval=pd.Series(dtype="boolean"), ax=None, gyro=True, controller=True):
        if interval.empty:
            interval = self.interval

        if ax == None:
            _, ax = plt.subplots()

        self.df[interval].plot(x='timestamp', y='odom_deg', ax=ax, label="odometry")
        if gyro:
            self.df[interval].plot(x='timestamp', y='gyro_deg', ax=ax, label="gyro")

        ax.set_ylabel("degrees")
        ax.set_xlabel("milliseconds")

        if controller:
            self.df[interval].plot(x='timestamp', y='hc_omega', ax=ax, secondary_y=True, label="controller omega")


    def subscription(self):
        sub = Subscription()
        tc = sub.measurable_by_type("frc.robot.commands.DriveTrajectoryCommand")
        ds = sub.measurable_by_type("frc.robot.subsystems.DriveSubsystem")
        fxs = filter(
            lambda item: item.type
            == "org.strykeforce.thirdcoast.talon.TalonFXMeasurable",
            sub.measurables,
        )
        sub.append(tc.id, Measure.TRAJECTORY_X.id)
        sub.append(tc.id, Measure.TRAJECTORY_Y.id)
        sub.append(tc.id, Measure.TRAJECTORY_VELOCITY.id)
        sub.append(tc.id, Measure.TRAJECTORY_ACCELERATION.id)
        sub.append(tc.id, Measure.TRAJECTORY_DEGREES.id)
        sub.append(tc.id, Measure.TRAJECTORY_TIME.id)
        sub.append(tc.id, Measure.HC_VY.id)
        sub.append(tc.id, Measure.HC_VX.id)
        sub.append(tc.id, Measure.HC_OMEGA.id)
        sub.append(ds.id, Measure.ODOMETRY_X.id)
        sub.append(ds.id, Measure.ODOMETRY_Y.id)
        sub.append(ds.id, Measure.GYRO_ROTATION2D_DEGREE.id)
        sub.append(ds.id, Measure.ODOMETRY_ROTATION2D_DEGREE.id)
        for fx in fxs:
            sub.append(fx.id, Measure.CLOSED_LOOP_TARGET.id)
        return sub

    def __repr__(self):
        return super().__repr__()
