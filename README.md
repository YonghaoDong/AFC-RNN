# AFC-RNN: Adaptive Forgetting-Controlled Recurrent Neural Network for Pedestrian Trajectory Prediction


    This is the official implementation for _**AFC-RNN: Adaptive Forgetting-Controlled Recurrent Neural Network for Pedestrian Trajectory Prediction  **_.]
    Only test code is released. The results in our paper can be reproduced by the checkpoints in '/models'.
    The training code will release after paper acceptance.

## Dependencies

- Pytorch 1.11
- Numpy 1.21

We recommend to install all the requirements through Conda by

    $ conda create --name <env> --file requirements.txt -c pytorch -c conda-forge

## Code Usage

## Training
Training code will come after paper acceptance. 

You can evaluate the pre-trained models as follows.

## Evaluation 

Command to evaluate a pre-trained model:

    $ python main.py --test <test_data_dir> --ckpt <checkpoint_dir> --config <config_file>

We provide our pretained models in `models` folder. To evaluate our pre-trained models, please run


    # ETH/UCY benchmarks
    $ python AFCRNN.py --test data/eth/test --ckpt models/eth --config config/eth.py
    $ python AFCRNN.py --test data/hotel/test --ckpt models/hotel --config config/hotel.py
    $ python AFCRNN.py --test data/univ/test --ckpt models/univ --config config/univ.py
    $ python AFCRNN.py --test data/zara01/test --ckpt models/zara01 --config config/zara01.py
    $ python AFCRNN.py --test data/zara02/test --ckpt models/zara02 --config config/zara02.py
    
    # SDD benchmark
    $ python AFCRNN.py --test data/sdd/test --ckpt models/sdd --config config/sdd_pixel.py
    
    # NBA benchmark
    $ python AFCRNN.py --test data/nba/rebound/test --ckpt models/nba/rebound --config config/nba_rebound.py
    $ python AFCRNN.py --test data/nba/score/test --ckpt models/nba/score --config config/nba_score.py



### Prepare your own dataset

    Datasets are in ‘/data’ file.


### Thanks

    Thanks to "SocialVAE: Human Trajectory Prediction using Timewise Latents". Part of codes are borrowed from them.# AFC-RNN
