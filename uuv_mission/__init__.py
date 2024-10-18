from dynamic import *
from terrain import *

sub = Submarine()
controller = Controller()
closed_loop = ClosedLoop(sub, controller)
mission = Mission.from_csv("data\mission.csv")

trajectory = closed_loop.simulate_with_random_disturbances(mission)
trajectory.plot_completed_mission(mission)