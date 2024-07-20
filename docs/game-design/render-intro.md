# What is rendering?

Rendering is the process of taking a scene and converting it into an image.

![](https://unity-connect-prd.storage.googleapis.com/20211125/learn/images/eef5c79e-b93b-4e62-9436-eb13bd2c237f_image22.png)

Let’s break it down even further:
In Unity, you can position 3D models, apply materials to those models, and point a virtual camera at them. Rendering is taking in all that data (object geometry, position, colors, lighting, and much more) and producing an image from the perspective of a camera. 

![](https://unity-connect-prd.storage.googleapis.com/20211125/learn/images/31381681-ff92-4efb-97b4-78f0abf30d44_image12.png)

## Render Pipeline

If rendering is the process of getting from point A to point B (3D data to a 2D image), then you can think of render pipelines as the different ways of getting there. 

![](https://unity-connect-prd.storage.googleapis.com/20211125/learn/images/c0124772-aba8-49de-abe0-e5b97ed2815e_image16.png)

Since each render pipeline uses different techniques and calculations to produce a 2D image, the results can vary, depending on which pipeline you choose. 
Choosing a render pipeline for your project is just like choosing whether to walk, cycle, or drive to your destination; no one option is inherently better or worse than the other – it just depends on your goals! 
And just as walking, cycling, and driving have advantages and disadvantages, so too do different render pipelines. One is fastest, one might be easiest, and sometimes, one won’t work at all for where you’re trying to go! That’s why it’s important to choose the render pipeline that best suits your goals for the project.

不同的渲染管线会产生不同的风格

## Render Pipeline in Unity

- Unity’s Built-In Render Pipeline works on all platforms and is pretty reliable. It’s easy to use, but it is built-in to Unity, so it’s not very customizable. It isn’t the most efficient, either.
- The Universal Render Pipeline (URP) is ideal for mobile, web, and VR projects, since it is highly optimized for performance. It’s a bit more complex to configure, but it is more customizable than the Built-In Render Pipeline. It can produce pretty decent graphics.
- The High Definition Render Pipeline (HDRP) is designed to produce high-quality graphics for high-end platforms, like consoles or gaming computers, where there is plenty of processing power. It is very complex to configure, so should only be used by people with lots of graphics experience.

Let’s immediately rule out HDRP, since we’re not targeting extremely high end machines and because it requires a lot of graphics expertise. 

独立项目别选HDRP

But how should you choose between the Built-In Render Pipeline and URP? Well the whole point of this pathway is for you to learn and experiment with the core features of Unity’s creative systems, including lighting, materials, post-processing, and visual effects. So here are some reasons to choose URP over the Built-In Render Pipeline:
URP更好

- URP is more customizable than the Built-In Renderer Pipeline, allowing you to experiment more.
- Some really powerful new editor features like Shader Graph and VFX Graph are only compatible with URP and not the Built-In Render Pipeline. 
- URP projects are optimized for performance on whichever platform you want to target (web, desktop, mobile, or VR). 

To sum up: HDRP is too fancy, and the Built-In Render Pipeline isn’t quite customizable enough for what we want to do – so we’ll use URP throughout this pathway.

![](https://unity-connect-prd.storage.googleapis.com/20211125/learn/images/2e3f88de-9d7e-4700-a3ea-c15817eaf1ed_image18.png)

# Unity Render Project

Create a new Unity project using the 3D Sample Scene(URP) template. Name it something like “GuidedProjectAlienVideoGameShop” (or whichever design document you selected).

Unity will open to a sample project to showcase URP’s features. Take a moment to admire the beautiful example scene that comes with the URP template.

From the main menu, select Edit > Project Settings > Quality. At the center of the panel, you will see Low, Medium, and High Quality Levels and a green checkbox indicating the default quality level for each target platform.

![](https://unity-connect-prd.storage.googleapis.com/20230804/learn/images/14370e7c-7ac9-4a5e-9be6-0a1c5e0405e3_image.png)

Click through the Low, Medium, and High settings and notice the changes in the Scene view, focusing on the shadows, lights, and reflections on the half-painted blue wall. 


![](https://unity-connect-prd.storage.googleapis.com/20211125/learn/images/b04aa54a-9f56-4f84-af64-ac360e392ee2_Screenshot_2021_11_25_at_16.59.59.png)

When you cycle through these quality settings, you are actually changing which URP Asset is used to render the scene.  

![](https://unity-connect-prd.storage.googleapis.com/20230804/learn/images/1699578a-39e7-4c69-a306-6fb164c8ef95_image.png)

URP Assets control many quality settings in your project – especially related to light and shadows – and can be found in the Project window just like any other asset. 

In the Quality Settings window, double-click the URP asset, which is named UniversalRP - High/Medium/LowQuality. 

This will locate the asset in the Project window and reveal its properties in the Inspector. Browse through the settings available in the URP asset, specifically those related to light and shadows. Don’t worry if you don’t understand what they all mean – you’ll learn more about these settings throughout the pathway. If you want to read about these settings in advance, check out the URP asset documentation.

# Free resource


[pexels](https://www.pexels.com/) 提供免费的 2D 图像和视频。本网站上的所有资产都具有相同的许可协议：它们可以免费使用，付款和归属是可选的。

[Creative Commons](https://search.creativecommons.org/) 搜索引擎允许您根据 Creative Common 许可证和来源过滤搜索。此站点索引图像、音频和视频文件。

[Open Game Art](https://opengameart.org/) 提供 2D 和 3D 艺术、纹理、音乐和声音效果。所有资产都是免费的;但是，有多种不同的许可证类型，因此请务必检查是否需要按资产注明创建者