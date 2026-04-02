# TensorOrder
A Python 3 tool for automatically contracting tensor networks for weighted model counting on multiple CPUs and on a GPU.

## Installation

Install system dependencies and Python packages:
```
sudo apt-get install -y libdbus-1-dev libglib2.0-dev metis libmetis-dev
pip install -r requirements.txt
```

Point the `metis` Python binding at the shared library (add to `~/.bashrc` to make it permanent):
```
export METIS_DLL=$(find /usr -name 'libmetis.so' 2>/dev/null | head -1)
```

Compile solvers and Cython extensions:
```
make -C solvers/flow-cutter-pace17
cd src && python setup.py build_ext --inplace
```

## Usage

```
python src/tensororder.py --planner="line-Flow" --weights="unweighted" \
  < benchmarks/cubic_vertex_cover/cubic_vc_50_0.cnf
```

The `--tensor_library` flag selects the backend (`numpy`, `tensorflow`, `jax`). Defaults to `numpy`.

## Other planners

Additional planners require their solvers to be compiled first:

- **KCMR-metis / KCMR-gn**: requires METIS (installed above via apt)
- **line-Tamaki / factor-Tamaki**: compile Tamaki with `make heuristic` in [solvers/TCS-Meiji](solvers/TCS-Meiji)
- **line-htd / factor-htd**: compile htd with `cmake . && make` in [solvers/htd-master](solvers/htd-master)
- **factor-hicks**: compile Hicks with `make` in [solvers/hicks](solvers/hicks)
- **line-portfolio3**: all solvers above must be compiled, then `make` in [solvers/portfolio](solvers/portfolio)

## Docker / Singularity

See [docker.md](docker.md) for container-based installation.

## Publications

Please cite the following article if you use our code in a publication:

* [Parallel Weighted Model Counting with Tensor Networks](https://arxiv.org/abs/2006.15512). Jeffrey M. Dudek and Moshe Y. Vardi. Proceedings of MCW'20.
