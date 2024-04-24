# Co2As

Cell dimensions:
a = 7.64 a0 (bohr radii) per cell
c = 11.34 a0 (bohr radii) per cell

For Co2As we differentiate between four configurations at the moment: single cell FM, single cell AFM, double cell FM, double cell AFM (uunnduddnnud).
The doubled cell AFM has upwards magnetisation on the Co atoms in the first plane. Then the cobalt in the inter-planar space, which is further from the first plane (and thus closer to the second plane) "goes down", and the other inter-planar cobalt (which is now closer to the first plane) "goes up". The cobalts in the second plane "go down" and so on...

The single cell calculations are done with 1000 k-points. Doubled cell are done with 500 k-points.

| Configuration           | E [Ry/cell]         | Mag. total [uB/cell] | Mag. Co in-plane [uB] | Mag. Co inter-planar [uB] |
| ----------------------- | ------------------- | -------------------- | --------------------- | ------------------------- |
| Sg. FM                  | **-20192.03199042** | 7.07705              | 1.67894               | 1.90676                   |
| Sg. AFM                 | -20192.00067364     | 0.00330              | 1.17251               | 1.88615                   |
| Dbl. FM                 | **-20192.03187535** | 7.06457              | 1.66442               | 1.90496                   |
| Dbl. AFM (uunnduddnnud) | -20192.00539123     | 0.00058              | 1.40825               | 1.85962                   |
