
import os
import rospkg

rospack = rospkg.RosPack()

DATASET_TEMPLATE_PATH = rospack.get_path('grasp_dataset')

DIR_PREFIX_LOCAL = rospack.get_path('data')
DIR_PREFIX_ELEMENTS = "/media/Elements/gdl_data/grasp_datasets/"

DIR_PREFIX = DIR_PREFIX_LOCAL + '/data/'

MESH_MODELS_DIR = os.path.expanduser(DIR_PREFIX + "mesh_models/")

RAW_GRASPIT_DIR = os.path.expanduser(DIR_PREFIX + "0_raw_graspit/")
AGG_GRASPIT_DIR = os.path.expanduser(DIR_PREFIX + "1_agg_graspit/")
RAW_GAZEBO_DIR = os.path.expanduser(DIR_PREFIX + "2_raw_gazebo/")
CONDENSED_GAZEBO_DIR = os.path.expanduser(DIR_PREFIX + "3_condensed_gazebo/")
RAW_PYLEARN_DIR = os.path.expanduser(DIR_PREFIX + "4_raw_pylearn/")
GRASP_PRIORS_DIR = os.path.expanduser(DIR_PREFIX_LOCAL + "5_grasp_priors/")
DEEP_MODELS_DIR = os.path.expanduser(DIR_PREFIX_LOCAL + "6_deep_models/")


TEST_DIR_PREFIX = DIR_PREFIX_LOCAL + '/test_data/'

TEST_RAW_GRASPIT_DIR = os.path.expanduser(TEST_DIR_PREFIX + "0_raw_graspit/")
TEST_AGG_GRASPIT_DIR = os.path.expanduser(TEST_DIR_PREFIX + "1_agg_graspit/")
TEST_RAW_GAZEBO_DIR = os.path.expanduser(TEST_DIR_PREFIX + "2_raw_gazebo/")
TEST_CONDENSED_GAZEBO_DIR = os.path.expanduser(TEST_DIR_PREFIX + "3_condensed_gazebo/")
TEST_RAW_PYLEARN_DIR = os.path.expanduser(TEST_DIR_PREFIX + "4_raw_pylearn/")
TEST_GRASP_PRIORS_DIR = os.path.expanduser(TEST_DIR_PREFIX + "5_grasp_priors/")
TEST_DEEP_MODELS_DIR = os.path.expanduser(TEST_DIR_PREFIX + "6_deep_models/")
