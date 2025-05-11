from numpy.typing import NDArray
from typing import Annotated
import numpy as np

Vector3D = Annotated[NDArray[np.floating], (3,)]
