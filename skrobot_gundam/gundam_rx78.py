from io import BytesIO as StringIO
import os

from skrobot.models.urdf import RobotModelFromURDF


class GUNDAM_RX78(RobotModelFromURDF):

    def __init__(self, *args, **kwargs):

        if not ('urdf_file' in kwargs or 'urdf' in kwargs):
            kwargs['urdf'] = self._urdf()
        super(GUNDAM_RX78, self).__init__(*args, **kwargs)
        self.name = 'hsrb'

    def _urdf(self):
        import rospkg
        rospack = rospkg.RosPack()
        package_path = rospack.get_path('gundam_rx78_description')
        self.resolve_filepath = os.path.join(
            package_path, 'urdf', 'GGC_TestModel_rx78_20170112.urdf')
        with open(self.resolve_filepath, 'rb') as f:
            urdf_text = f.read()
        return urdf_text

    def load_urdf(self, urdf):
        f = StringIO()
        f.write(urdf)
        f.seek(0)
        f.name = self.resolve_filepath
        self.load_urdf_file(file_obj=f)
