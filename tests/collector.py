import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.resolve()
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from DataAcquisitionModule.Application.data_acquisition_service import DataAcquisitionService

if __name__ == "__main__":
    service = DataAcquisitionService(max_pages=20, max_depth=3, delay=1, batch_size=5)
    service.run()