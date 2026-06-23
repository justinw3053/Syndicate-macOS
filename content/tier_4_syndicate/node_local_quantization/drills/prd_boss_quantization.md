# PRD: 4-bit Min-Max Quantization
Compress 32-bit floats into 4-bit integers (0 to 15).
1. `quantize_4bit` returns a list of integers, the scale float, and the min weight float.
   - `S = (W_max - W_min) / 15`
   - `Q_i = round((W_i - W_min) / S)`
2. `dequantize_4bit` restores them.
   - `W_i = (Q_i * S) + W_min`
