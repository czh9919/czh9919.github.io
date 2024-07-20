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

