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

## Smoothness

我愿称这玩意儿为抛光度

Observe solidly colored materials in your own world: plastic, paper, ceramic. Notice the specular highlights. Are they blurry or focused? Can you see the light source in the reflection? What does this tell you about the smoothness or roughness of each object? 

Now consider the apples on your workbench. Their specular reflections are blurry highlights, which tells us that their surfaces are a little rough. But if we polish the apple to make the surface more glossy, we can see the shape of the light source reflected in the surface. 

Smoothness, also called gloss or glossiness, brings the specular reflection into focus. From a smooth surface, light reflects in a uniform way so that you can see the shape of the light source in the reflection.

From a rough surface, there is still a specular reflection, but it is scattered. Small surfaces all over the apple give off a specular reflection.

Smoothness increases the specular reflection, but it’s important not to confuse the two. High specularity makes an object look like metal. A surface can be very smooth, like our polished red apple, but still not look like metal. 

In the image below, all five apples have a Metallic setting of 0.5, with increasing smoothness. On the smoothest one, we can see the lights and reflection of the table.

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/44fb8267-f2b2-47ab-ac6c-16df97355fd1_CC_Shad_Light6.png)

## transparent and translucent effects to your materials 透明度

Transparency is controlled with the alpha channel of the base map (The A in RGBA). Low values make the base map color less visible and high values make it more visible. You can make a mesh entirely invisible by setting the alpha channel values to zero, or you can create translucent effects by setting the alpha values in the mid-range.

### Create a glass material

A perfectly clear and flat pane of glass has no diffuse reflection — all the light passes through it, and no color is reflected back to your eye. It does, however, have a specular reflection — light glints off its smooth surface. Glass in the real world is rarely perfectly clear; it has a tint and some imperfections, which create a slight diffuse reflection.
一点点镜面反射，绝大多数光线穿过

In the real world, translucent substances refract light, which means they change its direction. Refraction is an advanced shader effect that we won’t attempt here; however, we can create a translucent glass object that looks pretty convincing.  

打开一个材质，locate Surface Options (at the top of the Material section) and the Surface Type property. Change this value from Opaque to Transparent. Set Render Face to Both.不然只会渲染前半部分。

To adjust the alpha channel values, select the color picker for the Base Map. By default, the A channel is set to the highest value, 255, which allows no transparency. Use the slider or enter a number less than 255 to get the transparency to a level that makes the jar look like glass. (Be careful — at 0, it is totally invisible!)

Give it a little Metallic, even though it isn’t a metal, to enhance the specular reflection. 

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/68176252-e714-4788-894a-dfb30dba9adb_PlantInJarGlassOnly.png)

### Add detail with alpha clipping
Consider an object like the one below. It’s a simple object that a modeling artist could create by making a leaf-shaped mesh.

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/f3a6bfa6-c91f-408d-8a38-c1dc1f547752_Leaf.png)

However, for an object that will be small in the scene, and might even be used thousands of times (in a tree, for instance), this leaf’s mesh would require a lot of computing power to render.

Instead of modeling meshes of items like these, artists use alpha clipping in their textures to make part of a simple mesh invisible. Alpha clipping is a much more efficient way to create detailed objects — it’s easier to create and easier for the computer to process at runtime.

1.  In the Project window, open the Materials folder and create a new material. Name it “Leaf”.
2.  In the Hierarchy, expand the PlantInJar GameObject and locate the child GameObjects that have Leaf in their names. Select all of the leaves and the PlantStem.
3.  In the Inspector, in the Mesh Renderer component, you can use the circle icon under Materials to select one material for all the selected GameObjects. Select Leaf. 
Now, you only need to have one leaf selected in order to edit this material on all of the leaves.
4.  Examine the plant from all angles. The leaves are visible from the top, but not from the bottom! This happens because these meshes are single-sided: there is no separate mesh on the back of the object (as there is with a cube, for example). 
5.  In the Inspector, on your Leaf material, change the Render Face to Both to make the shader render both sides of each mesh.
6.  In the Project window, locate the texture Plant_Albedo by searching for it. Apply this texture as the Base Map in the Leaf material. 
The stem is now solid. Look closely at the texture and you’ll see a green stripe on the left side, which is mapped only to the PlantStem object, while the rest of the texture is mapped to the Leaf child objects. Mapping multiple objects on one texture is a technique artists use to reduce the number of files and overall file size of a project.
Now the leaves look like printouts of leaves on paper! You can fix that with alpha clipping.
7.  In the Inspector, examine the alpha channel of the Plant_Albedo texture. It is a cutout of the leaf. We’ll use this alpha channel to “cut out” the leaf in this material. 
8.  In Scene view, select the Leaf material and locate the Surface Options section at the top of  the Material Inspector, and enable Alpha Clipping.
9.  A Threshold slider appears. While examining a leaf closely, move this slider. At some threshold value, the “paper” around the leaves will disappear. 
10.  Adjust this value so that the edges of the leaves look right. If the Threshold is too low, then pixels at lower alpha channel values will be visible, and the white edge will appear. If it is too high, then some of the higher alpha channel values will be invisible, cutting off the edges too close and causing some holes.  

This piece is complete. It should look like the image below.

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/f63ac1f4-9373-4e03-bd19-e65c0ad10b4d_PlantInJar.png)

## Add physical texture with bump mapping

In addition to the properties we have covered so far, materials for physically based shaders allow you to add the illusion of physical texture to a simple mesh without complicating it with lots of detailed polygons. The process of using textures to add this detail is called bump mapping. This process is much more efficient than modelling small details on a mesh.

Consider the difference between a low-poly mesh (a mesh with fewer polygons) and a high-poly mesh. It takes more computing power to render a high-poly mesh because more polygons mean there is more data to process. 

But with bump mapping, you can tell the shader to add the appearance of surface detail to your mesh without actually adding polygons. This technique is better for performance, and the results can be pretty convincing!

[bump maps docs](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterNormalMap.html)

There are two types of maps primarily used in bump mapping: normal maps and height maps.

As you will recall, normals are values in the mesh data that define the direction each vertex is facing. A normal map sets these values over an entire surface, which directs the shader to create the illusion that fragments (pixels) on the surface are facing different directions.

Height maps indicate the relative height of each pixel from the mesh.
![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/1a10eda3-f94b-463c-a9ce-1e44c1226691_Copy_of_CC_Shad_Mesh_5.png)

Normal and height maps can add realistic physical details to your surfaces without using much computing power. Frequently, normal maps are used without height maps.

Like base maps and specular/metallic maps, normal maps are created in 3D modeling or painting software. You can even download tileable normal maps from the Unity Asset Store! 

A normal map is similar to a base map, except that the red, green, and blue values indicate the direction of the normal relative to the mesh surface. Normal maps are mostly cyan and purple because the directions are expressed using higher values in the blue channel.

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/5d4b3249-c40a-42dd-9232-5a66e331e9b6_CC_Shad_Bump_1.png)

Height maps indicate the relative height of each pixel from the mesh. These are single-channel (grayscale) maps in which each pixel value indicates a relative distance from the mesh surface. When you use an RGB image as a height map, the shader only reads the green channel.

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/879c1634-f637-4799-9db3-c157caf826c6_HeightMap_Pavement_TinyMoss_height.png)

Height maps are not used as commonly as normal maps. They are useful for creating a dramatic effect, but they also stretch the base map, which is not usually desirable if the base map is not a solid color. 



## Occlusion Map

Occlusion, in 3D graphics, is the blockage of light by an object. A crack in a sidewalk and the thin dark shadow line between the fingers of a closed fist are examples of occlusion.
Even in PBR, ambient light can reflect in odd ways where it should be occluded. An occlusion map adds shadows to these occluded areas.
Occlusion maps are produced along with most models in 3D modeling software. The effects are sometimes subtle, but they make the light on surfaces more realistic and can enhance detailed shadows in ways that base maps and bump mapping can’t.


## microsurface mapping

Look very closely at a real-world object that has a smooth surface, such as the glass on your smartphone, covered with fingerprints, or your favorite coffee cup that has become scratched and worn. If you wanted to model these items and include details like the fingerprints or scratches, you can use microsurface mapping to add a level of detail that isn’t otherwise captured in your base map or normal map.

There are two additional textures in the Detail Inputs section of the URP/Lit Shader materials:
- A Detail Inputs Base Map can add detailed color, such as threads in fabric. 
- The Mask is an alpha channel map that shields specified areas from the Base Map and Normal Map microsurface maps.

![](https://unity-connect-prd.storage.googleapis.com/20211123/learn/images/f4a34651-9aeb-4c68-a300-2b5167f848f8_CC_Shad_Ref_2.png)

