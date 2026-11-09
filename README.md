# Agricultural Aerial Vision

A computer vision project focused on analyzing aerial agricultural imagery using Python and OpenCV.

## Project Goal

Develop a system capable of analyzing agricultural fields from aerial images, estimating vegetation coverage, and eventually identifying regions that may require further inspection.

## Current Progress — Version 0.1

The first version implements:

- Aerial image loading and resizing.
- Vegetation segmentation using HSV color ranges.
- Agricultural parcel segmentation.
- Vegetation coverage estimation.
- Visualization of segmentation masks.

## Technologies

- Python
- OpenCV
- NumPy

## How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Place an agricultural image named `terrain.png` inside the `images/` directory.

Run the program from `src/`:

```bash
cd src
python3 vegetation_analysis.py
```

## Dataset

The project uses aerial agricultural imagery from the LAPIX Crop Rows Identification and Segmentation dataset.

Dataset: https://lapix.ufsc.br/crop-rows-sugar-cane/?lang=en

Images are not redistributed in this repository.

## Development Roadmap

- [x] Vegetation segmentation using HSV.
- [x] Parcel region identification.
- [x] Vegetation coverage estimation.
- [ ] Spatial vegetation coverage analysis.
- [ ] Crop row identification.
- [ ] Detection of vegetation irregularities.
- [ ] Inspection priority map generation.
- [ ] Evaluation of AI-based segmentation approaches.
- [ ] Future UAV simulation integration.

## Current Limitations

Vegetation is identified using manually selected HSV thresholds. Results may be affected by illumination, soil color, image resolution, and vegetation characteristics.

The current vegetation coverage percentage is an estimate based on color segmentation, not a measurement of crop health.

## Project Status

Version 0.1 — Initial development.