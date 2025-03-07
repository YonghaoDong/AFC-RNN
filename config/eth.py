# model
OB_RADIUS = 2       # observe radius, neighborhood radius
OB_HORIZON = 8      # number of observation frames
PRED_HORIZON = 12   # number of prediction frames
# group name of inclusive agents; leave empty to include all agents
# non-inclusive agents will appear as neighbors only
INCLUSIVE_GROUPS = []
RNN_HIDDEN_DIM = 256

# training
LEARNING_RATE = 1e-3 
BATCH_SIZE = 512
EPOCHS = 300       # total number of epochs for training
EPOCH_BATCHES = None # number of batches per epoch, None for data_length//batch_size
TEST_SINCE = 1   # the epoch after which performing testing during training

# testing
PRED_SAMPLES = 1   # best of N samples
FPC_SEARCH_RANGE = range(40, 50)   # FPC sampling rate

# evaluation
WORLD_SCALE = 1
