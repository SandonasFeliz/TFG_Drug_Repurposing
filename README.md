Bachelor's Thesis: *Design and development of a platform for the comparison and explanation of drug repurposing methods using biomedical networks and artificial intelligence.*

Drug repurposing looks for new therapeutic uses of medicines that are already known. This web application lets a user choose a disease and a biomedical dataset, runs several computational methods on a biomedical graph, and shows a ranking of candidate drugs for each method together with the evidence behind every result.

> **Disclaimer:** results are computational hypotheses to support research, not clinical recommendations.


## Planned features

- Use the default DISNET data or upload your own files.
- Validate the uploaded files and report errors clearly.
- Search a disease by name or identifier.
- Run the implemented methods and show one ranking per method on a single screen:
  - Gene/target overlap (Jaccard or hypergeometric test).
  - Network proximity (closest distance with z-score).
  - Embeddings and link prediction (if time allows).
- Compare the methods (common drugs in the top-N, rank correlation).
- Click on a drug to see its targets, its relation to the disease and the subgraph that supports it.
- Export the results as a PDF report.

## Tech stack

- Python 3.11
- [FastAPI](https://fastapi.tiangolo.com/) and [Uvicorn](https://www.uvicorn.org/)
- Jinja2 templates, plain CSS
- Planned: NetworkX, NumPy, pandas, SciPy, WeasyPrint

## Installation

Requires [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (or any Python 3.11 environment).

```bash
git clone <repository-url>
cd <repository-folder>

conda create -n tfg python=3.11 -y
conda activate tfg
pip install -r requirements.txt
```

## Run

From the project folder, with the environment active:

```bash
uvicorn main:app --reload
```

Then open <http://127.0.0.1:8000>. The automatic API documentation is available at <http://127.0.0.1:8000/docs>.

Press `Ctrl + C` to stop the server.

## Input data format

To use your own data, six tables are expected (CSV, TSV or JSON):

| Table | Columns |
|---|---|
| Diseases | `disease_id`, `disease_name` |
| Proteins | `protein_id`, `protein_name` |
| Drugs | `drug_id`, `drug_name` |
| Disease-protein associations | `disease_id`, `protein_id` |
| Drug-protein interactions | `drug_id`, `protein_id` |
| Protein-protein interactions | `protein_id_A`, `protein_id_B` |

Every identifier used in the relation tables must exist in the corresponding catalog table. Your own data and the default DISNET data are never mixed.

## Project structure

```
.
├── main.py              # FastAPI application and routes
├── requirements.txt     # Python dependencies
├── static/
│   └── style.css        # Styles
└── templates/
    ├── base.html        # Common layout (header and footer)
    ├── title_page.html
    ├── configuration_page.html
    ├── own_data_page.html
    └── disease_page.html
```

## Data sources and licenses

Default data: [DISNET](https://disnet.ctb.upm.es/) and other public sources. Please check the license of each source before reusing the data.

## Author

- Author: [Your name]
- Supervisor: [Supervisor name]
- University: [University and degree]
- Academic year: 2026

## License

[To be decided]
