## How does the HSV color space work?

1. **Divide $r, g, b$ by $255$**
2. **Compute $cmax$, $cmin$, difference**
* $cmax = \max(r,g,b)$
* $cmin = \min(r,g,b)$
* $\text{Diff} = cmax - cmin$


3. **Hue calculation:**
* if $cmax$ and $cmin$ are equal, then $h = 0$
* if $cmax$ equal $r$ then compute $h = (60 \times ((g - b) / \text{diff}) + 360) \pmod{360}$
* if $cmax$ equal $g$ then compute $h = (60 \times ((b - r) / \text{diff}) + 120) \pmod{360}$
* if $cmax$ equal $b$ then compute $h = (60 \times ((r - g) / \text{diff}) + 240) \pmod{360}$


4. **Saturation computation:**
* if $cmax = 0$, then $s = 0$
* if $cmax \neq 0$ then compute $s = (\text{diff}/cmax) \times 100$


5. **Value computation:**
* $v = cmax \times 100$