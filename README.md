# Oxford-IIIT Pet Semantic Segmentation

## Academic Deatils:
Student Name: Vibhor Shukla
Roll Number: 23115107
Branch: CSE
Semester: 7th
Institute: NIT Raipur

## Experiments
- Baseline encoder-decoder without skip connections.
- Same encoder-decoder with skip fusion.

## Quick Links:
Link to the Dataset: [Kaggle Dataset](https://www.kaggle.com/datasets/tanlikesmath/the-oxfordiiit-pet-dataset)

GitHub: [Project](https://github.com/VibhorShukla-BHRT/Pet-Segmentation-Experiment.git)

## Reproducibility settings
- Seed: 42
- Split: official trainval/test lists; trainval stratified 80/20 train/validation split
- Input: 128x128
- Batch size: 32; epochs: 20
- Optimizer: AdamW, lr=0.001, weight_decay=0.0001
- Loss: class-weighted CrossEntropyLoss
- Best checkpoint: highest validation mIoU

## Outputs
- `test_metrics.csv`: final held-out test metrics, including per-class IoU and mIoU
- `latency_measurements.csv`: measured model forward latency conditions
- `model_comparison.csv`: combined comparison table
- `*_training_log.csv`: epoch-wise logs
- `split_manifest.json`: exact train/validation/test image stems
- `experiment_config.json`: experiment configuration and environment
- `checkpoints/`: best validation checkpoints (large; do not commit unless needed)
- `plots/` and `predictions/`: plots and qualitative examples

## Important
Do not treat the test metrics as validation results. Checkpoint selection uses validation mIoU; the test set is evaluated after training. Latency numbers are hardware-dependent and exclude image loading and preprocessing.

## Reference
Parkhi, O. M., Vedaldi, A., Zisserman, A., and Jawahar, C. V. (2012). Cats and Dogs. IEEE Conference on Computer Vision and Pattern Recognition (CVPR).
