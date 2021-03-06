#Nr. of Simulation in MTCS
MCTS_NR   = 128 #256    

#Temperature for controlling exploration
MCTS_TAU  = 0.1

#Coefficient for U in Q+U
MCTS_U_COEFF = 1.0

####################################

# Number of features in each conv layer
MODEL_FEATNR = 32

# Number of hidden units in value head
MODEL_HIDDENNR = 32 #64

# Number of conv layers
MODEL_CONVNR = 5

####################################

# Number of stored states (not games)
PIPELINE_HISTORY_SIZE     = 100000 

# Batch size
PIPELINE_BATCH_SIZE       = 16 #256

# Evaluating the trained network after so many training steps
PIPELINE_TRAINING_LOOP_NR = 10 #1000

# Playing so many games with the current best model to generate training data
PIPELINE_SELFPLAY_NR      = 50 #100

# Playing so many games to decide if the trained modell is better than the best-so-far model
PIPELINE_EVAL_NR          = 20

# If the total result >= than the threshold, we consider the trained model better than the best-so-far model
# (Totalling: -1 - best-so-far model won; 0 - draw; +1 - trained model won)
PIPELINE_THRESHOLD        = 4
