import os.path
import torchreid


def main():
    datamanager = torchreid.data.VideoDataManager(
        root='./video_data/reid-data',
        sources='ilidsvid',
        targets='ilidsvid',
        height=128,
        width=128,
        batch_size_train=8,
        batch_size_test=8,
        transforms=['random_flip', 'random_crop']
    )
    models=['resnet50mid']
    for m in models:
        model = torchreid.models.build_model(
            name=m,
            num_classes=datamanager.num_train_pids,
            loss='tripet',
            pretrained=True
        )

        model = model.cuda()

        optimizer = torchreid.optim.build_optimizer(
            model,
            optim='adam',
            lr=0.0003
        )

        scheduler = torchreid.optim.build_lr_scheduler(
            optimizer,
            lr_scheduler='single_step',
            stepsize=20
        )

        engine = torchreid.engine.VideoSoftmaxEngine(
            datamanager,
            model,
            optimizer=optimizer,
            scheduler=scheduler,
            label_smooth=True
        )
        path=os.path.join('log',m,'tripet')
        engine.run(
            save_dir=path,
            max_epoch=60,
            eval_freq=10,
            print_freq=10,
            test_only=False
        )

if __name__=='__main__':
    main()