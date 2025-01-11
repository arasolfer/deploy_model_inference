# Deploy Demo: Model Inference

Repository for deploying the inference pipeline of a machine learning model.

## Table of Contents
- [Deploy Demo: Model Inference](#deploy-demo-model-inference)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Requirements](#requirements)
  - [Dependencies](#dependencies)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Output](#output)
  - [Notes](#notes)
  - [Contributing](#contributing)
  - [License](#license)

## Project Structure

```plaintext
deployment_ml/
├── data/                           # Input data folder 
├── models/                         # Scaler and trained models folder
├── src/                            # Source code
│   ├── data/                       # Data-related modules
│   │   ├── data_preprocessor.py    # Preprocesses and transforms input data
│   ├── model/                      # Model-related modules
│   │   ├── inference.py            # Runs model inference
│   │   ├── model_loader.py         # Loads the trained model
├── .gitignore                      # Specifies files and folders to ignore by Git
├── pyproject.toml                  # Poetry configuration
├── poetry.lock                     # Poetry dependencies
├── README.md                       # Project documentation (this file)
```

## Requirements
- Python 3.11 or higher
- Poetry for dependency management

## Dependencies
All dependencies are listed in `pyproject.toml`. Key libraries include:

- **pandas**: Data manipulation
- **scikit-learn**: Data preprocessing and evaluation utilities
- **joblib**: Model saving and loading

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/arasolfer/deploy_model_inference.git
   cd deploy_model_inference
   ```

2. **Install Dependencies:**

   Use Poetry to install all required dependencies:

   ```bash
   poetry install
   ```

3. **Prepare the Environment:**

   - Ensure the `data/` folder contains your input data for inference.
   - Place the trained model file in the `models/` folder.

## Usage

Run the inference pipeline using the following command:

```bash
poetry run python src/model/inference.py
```

## Output

The output of the inference pipeline will include:
- Predictions saved in a specified location (e.g., `data/processed/`).
- Logs detailing the inference process.

## Notes
- Ensure that the trained model is compatible with the input data.
- Modify the paths in the code if your data or model files are in different directories.

---

This pipeline is designed for extensibility and can be easily integrated into larger systems or deployed in production environments.

## Contributing

If you wish to contribute to this project:
1. Fork the repository.
2. Create a new branch for your changes:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Push your changes and open a Pull Request.

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

