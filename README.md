# Data Pipeline
Based on single image I/O. Could write for N image I/O.

## Project Structure
|name|item|description|
|-|-|-|
|images|image buckets|stores input images (ingest), writes to output images (normalized/generated)|
|notebooks|notebooks per action|experimenting with pipeline phases and data|
|test.py|test python script|generalized from the notebook, but not-production|
|production.py|production python script|lean and mean|

## Use Case: iterating over folder of updated imagery or video
- create training data
- control data fed model

## Pipeline (phase N because these can go in any order)
- PHASE 00: load from disk, display and save original
- PHASE 01: crop to object 
- PHASE 01: resize to 600 pixels (wide)
- PHASE 02: rotate in bounds
- PHASE N: flip
- PHASE N: crop
- PHASE N: arithmetic
- PHASE N: cleanup output image

## Use case: generate computer vision training data for identifying Littoral combat ships from aerial imagery
Could be used for training data or data ingest normalization of healthcare (pills / blood cells), automotive (license plates), etc.
1. Aircraft carriers
1. Amphibious warfare ships
1. Amphibious assault ships
1. Amphibious command ships
1. Amphibious transport docks
1. Dock landing ships
1. Expeditionary sea base
1. Cruisers
1. Destroyers
1. Frigates
1. **Littoral combat ships**
1. Mine countermeasures ships
1. Patrol ships
1. Submarines