from pathlib import Path

from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).parent

app = FastAPI(title="Drug repurposing platform")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
def title_page(request: Request):
    """P1: cover page (RF-01, RF-02)."""
    return templates.TemplateResponse(request, "title_page.html")


@app.get("/configuration")
def configuration_page(request: Request):
    """P2: do you want to use your own data? (RF-04, RF-05)."""
    return templates.TemplateResponse(request, "configuration_page.html")


@app.get("/configuration/own-data")
def own_data_page(request: Request):
    """'Yes' branch: upload the three files (RF-06)."""
    return templates.TemplateResponse(request, "own_data_page.html")


@app.get("/configuration/disease")
def disease_page(request: Request):
    """'No' branch (DISNET) and end of both branches: disease selection (RF-09)."""
    return templates.TemplateResponse(request, "disease_page.html")


@app.post("/configuration/own-data")
async def own_data_upload(
    disease_genes: UploadFile = File(...),
    drug_targets: UploadFile = File(...),
    ppi_network: UploadFile = File(...),
):
    """Receives the three files (RF-06).

    TODO: validate format, columns and identifiers (RF-07, RF-08) and
    store the files before continuing.
    """
    return RedirectResponse("/configuration/disease", status_code=303)