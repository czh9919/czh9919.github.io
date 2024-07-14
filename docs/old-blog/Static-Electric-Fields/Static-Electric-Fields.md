---
title: Static Electric Fields
catalog: true
date: 2018-11-11 13:11:53
mathjax: true
subtitle:
header-img:
tags: Field and Wave Electronmagnertics
---
# static electrc field

## Fundamental Postulates of Electrostatics in Free Space

**Electric field intensity** is defined as the force per unit charge that a small stationary test charge experiences when it is placed in a region where an electric field exists. That is,

$$
\vec{E}=\lim_{q\rightarrow 0}\frac{\vec{F}}{q}
$$

And given

$$
\nabla \cdot \vec{E}=\frac{\rho_v}{\epsilon_0}
$$

and

$$
\nabla \times \vec{E}=0
$$

Here\(\rho_v\) is the volume charge density of free charges, And \(\epsilon_0\) is permittivity of free space. And the equation asserts the static electric field is irrotational.
Proof:

$$
\text{in the spherical coordinates, we have}(u_1,u_2,u_3)=(r,\theta,\phi)\\\\\text{And we have }h_1=1,h_2=R,h_3=R\sin\theta\\\\
\text{so we have}\\\\
$$


$$
\nabla\times A=\frac{1}{R^2sin\theta}\begin{vmatrix} \vec{a_R} & \vec{a_\phi}R & a_\phi\sin\theta\\\\ \frac{\partial}{\partial R} & \frac{\partial}{\partial \theta} & \frac{\partial}{\partial \phi}\\\\ \vec{A_R} & R\vec{A_\theta} & R\sin \theta \vec{A}_\phi\end{vmatrix}\\\\
$$


$$
\text{for given A}\\\\
\nabla \times A=\begin{vmatrix} \vec{a_R} & \vec{a_\phi}R & a_\phi\sin\theta\\\\ \frac{\partial}{\partial R} & \frac{\partial}{\partial \theta} & \frac{\partial}{\partial \phi}\\\\ f(R) & 0&0\end{vmatrix}=0
$$

With the two equation, we can use them to derive all other relations, laws, and theorem in electrostatics.
First, we take the volume integral of both sides of the equation.
$$
\int_V {\nabla\cdot\vec{E}dv}=\frac{1}{\epsilon_0}\int_V{\rho}dv
$$

Use divergence throrem, we get

$$
\oint_s{\vec{E}}ds=\frac{Q}{\epsilon_0}
$$

And this is Gauss's law.
And we take the volume integral of another equation. We get

$$
\oint_C{E\cdot dl}=0
$$

this asserts that the scaler line integral of the sstatic electric field intensity around any closed path vanishes.

## Coulomb's Law

First, we introduce a law, **The principle of conservation of charge**: The algebraic sum of all the electric charges in any closed system is constant(universal conservation law).
In order to find electric field intensity due to q, we draw a hypothetical enclosed surface(a Gaussian surface) around the source,then we use the Guass's law.

$$
\oint_S\vec{E}\cdot d\vec{s}=\oint_S{\vec{a_R}E_R\cdot\vec{a_R}ds}=\frac{q}{\epsilon_0},
$$

Then, we can get

$$
E_R\oint_Sds=E_R(4\pi R^2)=\frac{q}{\epsilon_0}
$$

Therefore,

$$
\vec{E}=\vec{a_R}E_R=\vec{a_R}\frac{q}{4\pi\epsilon_0 R^2}(V/m)
$$

This states that the force between two point charges is proportional to the product of the charges and inversely proportional to the square of the distance of separation.

## Gauss's Law

$$
\oint_S{\vec{E}\cdot d\vec{s}}=\frac{Q}{\epsilon_0}
$$
This states that the total outward flux of the E-field over any closed surface in free space is equal to the total charge enclosed in the surface divided by \(\epsilon_0\).

example:
<!-- ![ex1](1.png) -->

$$
\frac{\rho_1 L}{\epsilon_0}=\int_0^L\int_0^{2\pi}{\vec{E_r}rd\phi dz}
$$

## Electric Potential

The static electric field is a curl-free vector field, so it could be always expressed as the gradient of a scalar field.

$$
E=-\nabla \cdot V
$$

>注意三种坐标系的互化,就这样先