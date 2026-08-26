# Dog Breed Image Classifier

A Python project built as part of the **AWS AI & ML Scholars – Future AWS AI Programmer** 
program on Udacity. Uses pretrained CNN models to classify pet images and identify dog breeds.

## What It Does
- Identifies which images are dogs and which are not
- Classifies the breed of dog for dog images
- Compares performance across three CNN architectures

## Results (pet_images dataset)

| Model   | % Dogs Correct | % Breeds Correct | % Not-Dog Correct | % Match |
|---------|---------------|-----------------|------------------|---------|
| ResNet  | 100.0%        | 90.0%           | 90.0%            | 82.5%   |
| AlexNet | 100.0%        | 80.0%           | 100.0%           | 75.0%   |
| VGG     | 100.0%        | 93.3%           | 100.0%           | 87.5%   |

**Best Model: VGG** — achieved the highest breed classification accuracy (93.3%) while correctly identifying 100% of dog and non-dog images.

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/dog_breed_classifier.git
cd dog_breed_classifier
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
source .venv/bin/activate      # Mac/Linux
```

### 3. Install dependencies
```bash
pip install Pillow torch torchvision
```

### 4. Add your own pet_images folder, then run
```bash
cd data
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

## Files
- `check_images.py` — main program
- `get_input_args.py` — handles command line arguments
- `get_pet_labels.py` — extracts labels from image filenames
- `classify_images.py` — runs CNN classifier on images
- `adjust_results4_isadog.py` — flags images as dog or not-dog
- `calculates_results_stats.py` — computes accuracy statistics
- `print_results.py` — prints final summary

## Tools Used
- Python 3
- PyTorch
- torchvision (ResNet, AlexNet, VGG)
- Pillow (image processing)
