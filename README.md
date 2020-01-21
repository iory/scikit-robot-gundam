# scikit-robot for GUNDAM RX78

## Installtion

Build catkin workspace for [gundam_robot](https://github.com/gundam-global-challenge/gundam_robot).

After that,

```
git clone https://github.com/iory/scikit-robot-gundam
cd scikit-robot-gundam
python setup.py install
```

## Quick-Start

```
$ ipython
import skrobot
import skrobot_gundam

robot_model = skrobot_gundam.GUNDAM_RX78()

viewer = skrobot.viewers.TrimeshSceneViewer()
viewer.add(robot_model)
viewer.show()

print(robot_model.joint_list)
robot_model.init_pose()
robot_model.rarm_shoulder_r.joint_angle(-np.pi / 2.0)
robot_model.larm_shoulder_r.joint_angle(np.pi / 2.0)
```
