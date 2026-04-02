# Docker and Singularity

## Docker (CPU)

Build:
```
docker build --tag tensororder .
```

Run:
```
docker run -i tensororder python /src/tensororder.py \
  --planner="line-Flow" --weights="unweighted" \
  < benchmarks/cubic_vertex_cover/cubic_vc_50_0.cnf
```

For a TPU on Google Cloud:
```
docker run -i tensororder python /src/tensororder.py \
  --planner="line-Flow" --weights="unweighted" \
  --tensor_library="jax-tpu" --entry_type="float32" --tpu="<TPU_IP>" \
  < benchmarks/cubic_vertex_cover/cubic_vc_50_0.cnf
```

## Docker (GPU)

Requires [nvidia-container-runtime](https://nvidia.github.io/nvidia-container-runtime/).

Build:
```
docker build --tag tensororder-gpu -f Dockerfile-gpu .
```

Run:
```
docker run -i --gpus all tensororder-gpu python /src/tensororder.py \
  --planner="line-Flow" --weights="unweighted" --tensor_library="tensorflow-gpu" \
  < benchmarks/cubic_vertex_cover/cubic_vc_50_0.cnf
```

## Singularity

Build (from the repo root):
```
sudo singularity build tensororder Singularity
```

Run:
```
./tensororder --planner="line-Flow" --weights="unweighted" \
  < benchmarks/cubic_vertex_cover/cubic_vc_50_0.cnf
```
