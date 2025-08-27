# 5G-SDR
从零开始学习 5G NR 与软件无线电的渐进式实验仓库。包含 FM → OFDM → 5G PUSCH 完整链路，纯 Python/MATLab，注释清晰，可复现。Learning 5G NR &amp; SDR step-by-step.
# 5G-SDR

> 从零开始学习 5G NR 与软件无线电的渐进式实验仓库  
> Learning 5G NR & SDR step-by-step.

## 📂 项目结构
├── 01-FM-Radio/ FM 调频收音机（已完成） ├── 02-OFDM-BER/ OFDM 误码率曲线 ├── 03-5G-NR-PUSCH/ 5G NR PUSCH 链路 └── docs/ 中文实验手册
## 🚀 快速开始
```bash
git clone https://github.com/C2or/5G-SDR.git
cd 5G-SDR
pip install -r requirements.txt
python 01-FM-Radio/fm_receiver.py
