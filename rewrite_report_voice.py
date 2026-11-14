from pathlib import Path

from docx import Document


report_path = Path("23115107.docx")
document = Document(report_path)

# These replacements keep the report factual, but make the writing sound like a
# student explaining what was done and what was observed in this particular run.
replacements = {
    1: "Pet Image Segmentation Using an Encoder Decoder Network",
    2: "A comparison of a basic model and a model with skip fusion",
    7: (
        "For this project, I worked on semantic segmentation using the Oxford-IIIT Pet "
        "trimap dataset. I trained two small encoder-decoder models. The first model is "
        "the baseline. The second model uses skip fusion, where encoder features are passed "
        "to the decoder at matching resolutions. I kept the training setup the same for both "
        "runs so that the comparison stayed fair. On the official test set, the skip-fusion "
        "model gave an mIoU of 0.7337, compared with 0.7235 for the baseline. It did better "
        "on the boundary class too, although this came with extra parameters and higher latency. "
        "The prediction panels are also included because the averages alone do not show every "
        "type of mistake the models make."
    ),
    9: (
        "Semantic segmentation is different from normal image classification because the model "
        "has to decide the class of every pixel. In this case, it has to separate the pet, the "
        "background and the boundary around the pet. A model can identify the animal in general "
        "and still make visible mistakes around ears, legs or the outline, so the boundary class "
        "matters in this experiment."
    ),
    10: (
        "My main goal was to make a fair comparison instead of changing several things at once. "
        "Both models use the same split, image size, loss function, optimizer, random seed and "
        "number of epochs. The only planned difference is skip fusion in the second model. This "
        "makes it easier to relate the final difference in performance to that one architectural change."
    ),
    12: "Use the Oxford-IIIT Pet trimap labels and keep the official test set separate.",
    13: "Train a small encoder-decoder baseline and record the important settings.",
    14: "Add only skip fusion in the second model and compare it with the baseline.",
    15: "Compare both models with IoU, mIoU, parameter count, latency and saved prediction examples.",
    17: (
        "A segmentation model normally has two parts: an encoder and a decoder. The encoder reduces "
        "the image size step by step while learning useful features. The decoder brings the feature "
        "maps back to a higher resolution for pixel-wise prediction. The problem is that some fine "
        "detail can disappear while the image is being downsampled."
    ),
    18: (
        "Skip connections are one way of bringing some of that detail back. A feature map from an "
        "encoder layer is sent to the decoder layer with the same spatial size. The decoder can then "
        "use information from both the deeper layer and the earlier, higher-resolution layer. In my "
        "model, the feature maps are concatenated before the decoder block processes them."
    ),
    19: (
        "The Oxford-IIIT Pet dataset contains cat and dog images with trimap annotations. Each trimap "
        "has pet foreground, background and a boundary region. I used all three as classes. Keeping "
        "the boundary class is useful here because it tells us more about the quality of the predicted "
        "outline than a foreground-versus-background setup would."
    ),
    21: (
        "For one class, Intersection over Union is calculated as IoU_c = TP_c / (TP_c + FP_c + FN_c). "
        "The mIoU is the average of the three class IoUs. I used this along with pixel accuracy. Pixel "
        "accuracy by itself can look high when a model predicts the large background region well, so it "
        "does not tell the full story for this dataset."
    ),
    24: (
        "I used the Oxford-IIIT Pet official trainval and test lists. The trainval part was divided "
        "into training and validation data with a stratified 80:20 split using seed 42. This resulted "
        "in 2,944 training images and 736 validation images, while the official test set contains 3,669 "
        "images. The exact file stems are saved in split_manifest.json, so the same split can be used again."
    ),
    27: (
        "During training, I applied a random horizontal flip with probability 0.5 to the image and mask "
        "together. I also applied ColorJitter only to the image. The images were normalized using the "
        "ImageNet mean [0.485, 0.456, 0.406] and standard deviation [0.229, 0.224, 0.225]. The masks were "
        "resized with nearest-neighbor interpolation so that their class values would not change."
    ),
    29: (
        "Both models have three encoder stages with 32, 64 and 128 channels, followed by a 256-channel "
        "bottleneck. Every ConvBlock has two 3 x 3 convolution layers with batch normalization and ReLU. "
        "Max pooling reduces the resolution in the encoder, and bilinear interpolation increases it in "
        "the decoder. A final 1 x 1 convolution gives the three class scores for every pixel."
    ),
    32: (
        "In the baseline model, each decoder block receives only the feature map coming from the deeper "
        "decoder stage. In the skip-fusion version, I concatenate that upsampled map with the encoder map "
        "at the same resolution. This happens at 32 x 32, 64 x 64 and 128 x 128. Apart from these extra "
        "connections, the two models are the same."
    ),
    36: (
        "I calculated the class weights from the training masks only. This avoids using validation or test "
        "information while training. I saved the checkpoint with the highest validation mIoU and used that "
        "checkpoint for the final official test evaluation. The test set was not used to choose a model."
    ),
    38: (
        "For the final comparison, I reported class-wise IoU, mIoU, pixel accuracy and test loss. I also "
        "counted the trainable parameters. Latency was measured with one 128 x 128 image at a time on CUDA, "
        "after 20 warm-up runs and across 100 timed forward passes. These numbers only cover the model forward "
        "pass; loading images and preprocessing are not included."
    ),
    43: (
        "The skip-fusion model performed a little better on every class. The mIoU increased by 0.0102, and "
        "pixel accuracy increased by 0.0048. The biggest class-wise change is at the boundary: its IoU goes "
        "from 0.5033 to 0.5236. This is the result I expected to see if the extra high-resolution features "
        "were helping the decoder make cleaner boundaries."
    ),
    44: (
        "The gain also has a cost. Skip fusion adds 193,536 trainable parameters, which is about an 11.0% "
        "increase over the baseline. On the Tesla T4 used for the timing test, its forward time went from "
        "3.047 ms to 4.255 ms per image. That is 1.208 ms more per image. Whether this is acceptable depends "
        "on the use case, but it is worth keeping in mind if fast inference is important."
    ),
    47: (
        "The validation curves rise quickly during the first part of training and then become flatter. At the "
        "end of the 20 epochs, validation mIoU is 0.7126 for the baseline and 0.7237 for skip fusion. Both "
        "best checkpoints occurred at epoch 20. This does not prove that training longer would help, but it "
        "does show that skip fusion kept a small advantage under the same fixed budget."
    ),
    53: (
        "The sample predictions help explain the numbers in the table. In the close-up example, both models "
        "get the main shape of the dog, though the skip-fusion output keeps some local details better. The snow "
        "scene is harder. Both models find the dog, but parts of the snow and background are also predicted as "
        "pet or boundary. So even though mIoU improves, the model can still be confused by texture and low contrast."
    ),
    59: (
        "The failure example is important because it shows what the average result hides. On this test image, "
        "the trimap is background only, but both models predict a large foreground area. The skip-fusion model "
        "still makes this mistake. This may be because the texture resembles fur, or simply because a small model "
        "at 128 x 128 does not have enough detail for every unusual image. Based on this experiment alone, I cannot "
        "claim that skip fusion will be better for every image, every architecture or every hardware setup."
    ),
    61: (
        "I completed a three-class pet segmentation experiment using the Oxford-IIIT Pet trimaps. The main "
        "change I tested was skip fusion. It improved the held-out mIoU from 0.7235 to 0.7337, and the boundary "
        "class improved the most. The trade-off was a slightly larger model and a slower measured forward pass on "
        "the Tesla T4."
    ),
    62: (
        "For this particular setup, I would choose skip fusion when the extra 1.208 ms per image is acceptable. "
        "It gives a consistent, though not huge, improvement over the baseline. A useful next step would be to try "
        "a larger input size, add more augmentation, measure full end-to-end time, and look at errors by scene type "
        "or pet size. That would give a clearer idea of where the added connections help most."
    ),
    68: (
        "The repository includes the notebook, split manifest, configuration file, training logs, best checkpoints, "
        "test metrics, latency measurements, validation plots and saved prediction panels. Together, these files make "
        "it possible to check the reported setup and repeat the comparison."
    ),
}

for index, text in replacements.items():
    paragraph = document.paragraphs[index]
    paragraph.clear()
    paragraph.add_run(text)

# The final table fits on page 7, while its standalone caption created an empty
# page 8. Remove the redundant caption so the document ends with the appendix table.
for paragraph in list(document.paragraphs):
    if paragraph.text.startswith("Table 4. Repository artefacts supporting"):
        paragraph._element.getparent().remove(paragraph._element)
        break

for paragraph in reversed(document.paragraphs):
    if not paragraph.text.strip():
        paragraph._element.getparent().remove(paragraph._element)
        break

document.core_properties.author = "Vibhor Shukla"
document.save(report_path)
print(report_path.resolve())
