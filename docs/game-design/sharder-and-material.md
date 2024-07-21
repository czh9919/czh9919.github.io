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

## Relationship between Shaders and Materials

Shaders can be very specific or quite versatile. A shader can set the color of GameObjects or it can allow color to be configurable by materials. In fact, one shader can make many objects look like entirely different substances, while still giving a scene a unified look. 
In our gallery, everything you see uses the URP/Lit shader! What makes each of these GameObjects look different are the properties provided by the materials to the shader, including color and smoothness. 
Shaders and materials work together as a team — the shader defines what a surface can look like, while the material defines what it does look like.


Each material is written specifically for a certain shader. It’s common practice to import assets from one project into another, but sometimes the render pipelines of those projects don’t match and therefore neither do the shaders. When a material has a shader that is mismatched to the current render pipeline, it is bright magenta (pink) to alert you.

将普通project工程导入urp工程时需注意改变sharder

单个物体改变，From the Shader dropdown, select Universal Render Pipeline > Lit. 

多个物品自动改变，

1.  From the main menu, navigate to Window > Rendering > Render Pipeline Converter to open the Render Pipeline Converter window. This window allows you to update several types of assets to the latest URP standards.
2.  Near the top of the window is a dropdown menu that reads Convert Built-in to 2D (URP) by default. Change this setting to Built-in to URP. The items in the window will change.
3.  Scroll down to find the Material Upgrade section of the window, and enable that section.
4.  Select Initialize Converters at the bottom of the window. The list of materials to be upgraded will appear in the Material Upgrade section.

Tip: You can also upgrade a single material.  Select the material in the Project window, and then go to the main menu and select Edit > Rendering > Materials > Convert Selected Built-in Materials to URP.

# Light Behaves

When light comes in contact with any object, it can do one of three things: bounce off of it, which is known as reflection; pass through it, if the object is transparent or translucent; or be absorbed by it.

The way an object looks to the human eye depends on how it responds to light in some combination of these ways. We’ll use the apple on your workbench to demonstrate the ways light behaves on surfaces and the ways Unity simulates that behaviour.

### Specular and diffuse reflections

There are two ways that light reflects from an object: there are specular reflections and diffuse reflections.镜面反射和漫反射

A specular reflection is the direct reflection that is most visible on shiny objects. In the example image below, the specular reflection is white, which indicates that the light source is white. 

But not all the light that reaches the apple bounces off it directly. Other light penetrates the surface, and passes through or bounces around the outer layers of the apple. Some of this light is absorbed and some bounces out. The light that escapes is the diffuse reflection.

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/c0317228-05b2-42de-a315-230d93dcc0bf_CC_Shad_Light2.png)

The diffuse reflection of an object determines its visible color. On the apple, the non-red light is absorbed, and the red light is reflected to our eyes.

All together, the specular and diffuse reflections make up the total reflectivity of the surface. All reflected light is either specular or diffuse. 

## Diffuse reflectivity: the base map

In Unity, to represent diffuse reflectivity the URP/Lit Shader calls for a Base Map, which you have already used. Other shaders commonly call this property Albedo or Diffuse Map (even though, technically, these terms don’t mean exactly the same thing). 

### What is albedo?

The term albedo describes the measurement of diffuse reflection. It is typically specified as a regular color, expressed as three values for red, green, and blue (RGB values). RGB values can be translated to values for hue, saturation, and luminosity (brightness). The luminosity of the albedo color corresponds to the amount of diffuse reflection, and the hue and saturation describe the quality of light that escapes from the surface.

### Why is it called a map?

We will discuss mapping in more detail soon. Maps can be solid colors or they can be specified with 2D images to add variation to a surface. The color picker you have been using to set the Base Map property applies the selected color as a solid only.

## Metals in the Specular workflow

Take a look at the metal objects that you can see in the real world around you right now. These might include a pen, a rivet on your bag or clothing, or some jewelry. How would you explain metal in terms of specular and diffuse reflectivity? It’s a trick question, because metals don’t have much, if any, diffuse reflection!

What if the apple in your scene was an apple-shaped paperweight made of steel? It would no longer have a red color — all of its reflection is specular, whether it comes directly from the light source or indirectly from the environment. In fact, you would see every source of direct or indirect light as specular reflections over the entire surface.

The property of a surface that makes it look like metal is called specularity. 镜面反射

You can tell that a reflection is specular when you can see the source of the light reflected in the object. With untinted metals, like silver and steel, the light we see has the colors of the light that hits the surface, just like a mirror.

Specularity is different from smoothness. We could polish a red apple until it is very smooth, but it would never turn into metal that way. However, to have any specular reflection, a smooth object must have some specularity.

The apples in the image below have the same smoothness, but increasing levels of specularity.

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/0f9386fc-dcfe-42ab-bf95-7278dd8defe5_CC_Shad_Light3.png)

Like diffuse surfaces, metals do absorb light. You can tell this is true if you leave a metal object in the sun — it gets hot! But on colored metals, like gold and copper, the colored light we see is actually not a diffuse reflection — it is a tinted specular reflection. It must be specular because you can see the light sources in that reflection. The tint that you see is caused by the object absorbing part of the visible spectrum of light and only reflecting the tint color.

### Specular workflow 非金属工作流程

Specularity, as a property of a material, is one way to specify that a surface looks metallic. There are two workflows you can use to specify a metallic appearance in your materials. When you use the Specularity property in the URP/Lit shader, you are using the Specular workflow.

In the Specular workflow, smooth materials with a Specular setting greater than 0 will have some specular reflection.  

In the Specular workflow:
- A shiny metal has a high Specularity setting and a high Smoothness setting. 金属有更高的镜面反射和更高的平滑度
- A shiny non-metal has a low Specularity setting and a high Smoothness setting. 闪亮的非金属具有低镜面反射度设置和高平滑度设置
- Smoothness focuses the specular reflection, and the Specular Map controls the amount and color of the specular reflection. “平滑度”聚焦镜面反射  ，“镜面贴图”控制镜面反射的数量和颜色。 平滑度反射的光更多，镜面贴图更有金属质感
- The Specular Map can use RGB colors.


## Metals in the Metallic workflow 感觉这玩意儿是金属材质

Unity provides two ways to make objects look metallic. The Specular workflow, which you have been using, is the more scientific of the two. The Metallic workflow is simpler, but doesn’t strictly follow the rules of physical light. 


The base map color in the Metallic workflow remains visible in objects with a high Metallic setting. Compare the apples in the Specular workflow, above, with those in the Metallic workflow, below.

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/f611af4d-e29e-4e9e-aabb-4f17991a643c_CC_Shad_Light4.png)

In the Metallic workflow:
- A shiny metal has a high Metallic setting and a high Smoothness setting.
- A shiny non-metal has a zero or low Metallic value and a high Smoothness value.
- Smoothness controls the focus of the specular reflection.
- The Metallic map only uses grayscale. 

Here is a table to compare the two:

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/0039d601-b409-45f6-9c0d-b22a2ef0d907_CC_Shad_Light5.png)

### Smoothness

我愿称这玩意儿为抛光度

Observe solidly colored materials in your own world: plastic, paper, ceramic. Notice the specular highlights. Are they blurry or focused? Can you see the light source in the reflection? What does this tell you about the smoothness or roughness of each object? 

Now consider the apples on your workbench. Their specular reflections are blurry highlights, which tells us that their surfaces are a little rough. But if we polish the apple to make the surface more glossy, we can see the shape of the light source reflected in the surface. 

Smoothness, also called gloss or glossiness, brings the specular reflection into focus. From a smooth surface, light reflects in a uniform way so that you can see the shape of the light source in the reflection.

From a rough surface, there is still a specular reflection, but it is scattered. Small surfaces all over the apple give off a specular reflection.

Smoothness increases the specular reflection, but it’s important not to confuse the two. High specularity makes an object look like metal. A surface can be very smooth, like our polished red apple, but still not look like metal. 

In the image below, all five apples have a Metallic setting of 0.5, with increasing smoothness. On the smoothest one, we can see the lights and reflection of the table.

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/44fb8267-f2b2-47ab-ac6c-16df97355fd1_CC_Shad_Light6.png)

