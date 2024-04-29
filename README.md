# SpeechUnderstandingMajorProject
## Feature Extraction
For feature extraction use: \
(A) F0: \
    f0_extract.py in-dir out-dir \
(B) Energy: \
\t    energy_extract.py in-dir out-dir \
(C) Duration HuBERT: \
\t    encode.py --extension discrete in-dir out-dir
(D) XLS-R: \
\t xlsr_extract.py data-manifest-folder --path model-path \
        --task audio_classification --batch-size 90 \
        --infer-manifest /fsx/data/VoxLingua107/manifest/test.tsv \
        --infer-xtimes 10 --infer-max-sample-size 160000 --output-path out-dir \
\t Download: https://dl.fbaipublicfiles.com/fairseq/wav2vec/xlsr_300m_voxlingua107_ft.pt at model-path \

For training use:\
main.py [options]\

*IMPORTANT*: change LOSS function in config.py. Last function defines the LOSS currently as BCE change it as per requirements.
