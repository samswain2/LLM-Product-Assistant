# Assignment 2: Deep Q-Network - Wencheng Zhang
This repository is for HW2 (MLDS490-Advanced Algorithm). It implements DQN to solve cartpole-v0 and mspacman-v0 by using GPU and Python


## Directory structure 

```
├── README.md                                          <- You are here
│
│
├── cartpole-v0/                                       <- Folder that contains solution for CartPole-v0
│   ├── cartpole.py                                    <- python scripts for training DQN
│   ├── cartpole_dqn.h5                                <- trained DQN model
│   ├── cartpole_sample.py                             <- python scripts for sampling 500 episodes
│   ├── episode_reward_output.png                      <- episodes reward plot
│   ├── histogram_output.png                           <- histogram of 500 episodes
│   ├── max_q_values_output.png                        <- max-q-value plot
│   ├── requirements.txt                               <- packages requirements
│   ├── results_records.txt                            <- training records
│
│
├── mspacman-v0/                                       <- Folder that contains solution for mspacma-v0
│   ├── dnn_1000_noclip_decay_lr_50000.py              <- python scripts for training DQN
│   ├── hist_reward_dist.png                           <- histogram of 500 episodes
│   ├── mspacman_dqn.h5                                <- trained DQN algorithm
│   ├── mspacman_sample.py                             <- python scripts for sampling 500 episodes
│   ├── plot_episode_rewards.png                       <- episodes reward plot
│   ├── plot_max_q_value_200.png                       <- max-q-value plot
│   ├── requirements.txt                               <- packages requirements
│   ├── sample_records.txt                             <- inference records
│   ├── training_records.txt                           <- training records
 
```

## Environment Set up
To execute the code, follow these steps for each environment. Ensure you're starting in the directory containing the cartpole-v0 and mspacman-v0 folders.

#### Running cartpole-v0
Building computing environments for cartpole-v0
```bash
cd cartpole-v0
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

Use the following commands to conduct training process
```bash
python3 cartpole.py
```

Use the following commands to conduct inference process for 500 episodes
```bash
python3 cartpole_sample.py
```


#### Running mspacman-v0
Similarly, to run the mspacman-v0 simulation, use the following commands:

Building computing environments for mspacman-v0
```bash
cd mspacman-v0
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

Use the following commands to conduct training process
```bash
python3 dnn_1000_noclip_decay_lr_50000.py
```

Use the following commands to conduct inference process for 500 episodes
```bash
python3 mspacman_sample.py
```
