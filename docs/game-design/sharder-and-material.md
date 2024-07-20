# sharder and material

Shaders and materials let you define how your 3D objects look: their colors, reflectivity, and physical texture. With shaders and materials, you can bring realism into your projects or express your own artistic style.


## Sharder

A shader is a script that applies the properties contained in a material to render the meshes of your 3D objects to the 2D image on your screen. Each shader is written for a specific render pipeline. 

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/f9a7bbfa-9e76-42f3-bf2c-7ef4bdd896a9_CC_Shad_Shdrs_1.png)

The shaders you use depend on your render pipeline. In Unity, each template comes with shaders designed specifically for the render pipeline used in the template. 

### Type of Sharder

Overall, there are two types of operations that occur in a shader: fragment shading and vertex shading. 

Fragment shading, also known as pixel shading, is the shading that represents mesh surfaces to produce the color of each pixel in the 2D image. In this project, we’ll be working with fragment shaders and discussing in detail how they render with the light in the scene.

Vertex shading operates on the vertices of the mesh, typically changing their locations to make the surface move or transform.

### Physically based shaders and rendering

As computers have become more powerful and rendering technology has evolved, Physically Based Rendering (PBR) has become more widely available. PBR simulates the real-world principles of physics and light to generate realistic shadows, reflections, ambient light, and other effects of light on 3D surfaces. 

As computers have become more powerful and rendering technology has evolved, Physically Based Rendering (PBR) has become more widely available. PBR simulates the real-world principles of physics and light to generate realistic shadows, reflections, ambient light, and other effects of light on 3D surfaces. 

[StandardShaderMetallicVsSpecular](https://docs.unity3d.com/Manual/StandardShaderMetallicVsSpecular.html)

With PBR, the properties of lights and surfaces stay separate. Lights are defined in terms of their brightness, color, and range. Surfaces are defined, using materials, in terms of color, reflectivity, and other real-world properties that affect how light behaves on them. (You’ll learn about these real-world properties in this learning experience.) Then, the shader calculates the quality of light that bounces off surfaces based on the lights, surfaces, and 3D geometry of the scene, among other factors.

In the image below, the appearance of each surface changes as the light changes in the scene. The properties of the surfaces are the same in each image — it is only the color and direction of the light that is changing.

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/77875b15-bebe-427b-a7d9-5c436beff2c3_PBRExample.gif)

On the other hand, with non-Physically Based Rendering, the rendered colors, shadows, and reflections are either approximated without the science of PBR or just not rendered. With a non-PBR shader, a red material might render as a flat red color or with simple reflections and shadows. Non-PBR usually doesn’t look as realistic as PBR, but it can be more desirable for stylized effects. Toon shaders, which make surfaces in a 3D scene look like 2D cartoons, is one type of non-PBR shader.

[](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/3a75d4d2-9fb0-4d3c-b32f-1a06e8aeae58_AGredo.png)

For the shaders from the Universal Render Pipeline submenu,

- 2D > Sprite-Lit-Default: Designed for 2D projects, this shader is for flat objects only and will render any 3D object as 2D. As a lit shader, it will render based on the light in the scene that reaches the object.
- Particles > Lit, Simple Lit, and Unlit: These shaders are for visual effects (VFX). In the Creative Core pathway, you will use these shaders in the VFX mission.
- Terrain > Lit: This shader is optimized for use with the Terrain tools in Unity. In the Creative Core pathway, you will use this shader in the Prototyping mission.
- Baked Lit: This shader is automatically applied to lightmaps, which you will encounter in the Creative Core pathway’s Lighting mission.
- Complex Lit, Lit, and Simple Lit: These are all variations on a general-purpose, physically based lit shader. 
- Unlit: As described above, a shader that does not use light.