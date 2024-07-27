# Sharder Graph

There are many interesting effects you can create with shaders and materials, and you are not limited to the shaders that Unity provides. Shaders are scripts that you can manipulate if you know the coding language. Although learning that language is outside the scope of these tutorials, there is a tool that makes coding shaders easier: Shader Graph.

Shader Graph allows you to create specialized shaders without the need to write code. In particular, you can combine textures and make them move in a fragment shader or even change the positions of vertices in a vertex shader. Professional technical artists create custom shaders to implement specialized artistic styles and to create complex substances like flowing lava, storm clouds, and vegetation. The possibilities are nearly endless!

这是个新东西，以前没见过

![](https://unity-connect-prd.storage.googleapis.com/20211123/learn/images/e490d65c-a67a-4aa9-a155-9f534e5bf047_CC_Shad_SG_2_2.jpg)

- The Shader Graph toolbar (1) is where you will save your shader asset.
- The Blackboard (2) contains the properties that will be available to artists who use this shader to create materials. Here you can define property types as well as their names, attributes, and default values.
- Your workspace (3) is where you will create the node graph of your shader. 
- The Main Preview window (4) will give you a real-time update of what your shader looks like and how it behaves.
- The Graph Inspector window (5) will show you the current settings, properties, and values of any node you have selected.
- The Master Stack (6) is the end point of a Shader Graph that defines the final surface appearance of a shader. It lists the major shader properties of a Vertex and a Fragment shader and provides you with the end nodes where you will plug in the necessary values. 

### Procedural Map

The goal of this tutorial is to create a custom shader with a glowing, transparent, shimmering effect. You can follow these steps to re-create the shader in the gallery — or feel free to experiment as you go!

The basic shimmer is made with a procedural noise map. Procedural means that the texture is created by some formula or algorithm, not from an image or other physical source. Shader Graph provides a few procedural noise maps to choose from. Each one generates a cloud-like map with lighter and darker areas in a seemingly random pattern.

这个part感觉看文档更好，图形化编程感觉有点脱裤子放屁

习题

What is a mesh? 
The geometric data of a GameObject, consisting of vertices and normals.

The URP/Lit Shader calls for a Base Map to specify color. Other shaders commonly call this property Albedo or Diffuse Map (even though, technically, these terms don’t mean exactly the same thing).

Lit shaders respond to the light in the scene, and unlit shaders don’t. Unlit shaders are useful for certain artistic effects or for optimized projects that run more efficiently by not using lighting.

PBR simulates the real-world principles of physics and light to generate realistic shadows, reflections, ambient light, and other effects of light on 3D surfaces.

法线是网格数据中的值，用于定义每个顶点所面向的方向。法线贴图在整个表面上设置这些值。高度贴图表示每个像素与网格的相对高度。
Normals are values in the mesh data that define the direction each vertex is facing. A normal map sets these values over an entire surface. Height maps indicate the relative height of each pixel from the mesh.


The mesh is the 3D skeleton of your GameObject. It consists of vertices that define polygons, and normals that specify the directions vertices face. Every GameObject in Unity has a mesh. It is the geometric element of the object.

When a material is built for a shader of a different render pipeline than the current project, it is bright magenta (pink) to alert you.