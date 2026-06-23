import pytest
import active_lab

def test_quantization():
    original_weights = [0.8732, -0.1245, 0.5511]
    quantized, scale, w_min = active_lab.quantize_4bit(original_weights)
    reconstructed = active_lab.dequantize_4bit(quantized, scale, w_min)
    
    for orig, recon in zip(original_weights, reconstructed):
        assert abs(orig - recon) < 0.05, f"Loss too high: {orig} vs {recon}"
