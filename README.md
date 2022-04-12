# Video_based_ReID
Code implemented based on [Deep Person ReID](https://github.com/KaiyangZhou/deep-person-reid).
## How to run
1. conda create --name your-virtual-name python=3.7
2. pip install -r requirement.txt
3. conda install your-version-pytorch
4. python demo.py (set test-only to true)
## Findings & Results
Trained and tested 6 different models with different loss function on iLIDS Video Dataset. All models are trained with same hyper-parameter to compare performance:
batch size:8, image size:128*128, epoch:60, optimizer: adam, start learning rate: 0.0001
The results shown as follows:

| Model        |  mAP  |  Rank 1|
| :--------  | :-----  | :----:  | :----:  |
| OSNet _x1_0 (S) | 0.7328 |0.6267|
| OSNet _x1_0 (T) | 0.727 |0.6333|
| ResNet50Mid(S) | 0.7596 |0.6467|
| ResNet50Mid(T) | 0.778 |0.68|
| HACNN (S) | 0.5718|0.46|
| PCB_P4 (S) | 0.7329|0.6333|
|ResNet101(S) | 0.6675|0.5533|

The reason why choose these models is to compare the the types of classification method and ReID specific one since
the task is video-based with single camera, I want to prove that the models using the spatial and temporal information
within the video (ResNet50Mid) could have better performance compared with other single-frame models (ResNet101).

## Reasons of Implementation
I choose [Deep Person ReID](https://github.com/KaiyangZhou/deep-person-reid) because it support different dataset with
uniform user interface, which helps me to compare different models' performance easily.