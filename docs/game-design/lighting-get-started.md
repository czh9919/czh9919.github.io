# Lighting 

Light in Unity (and many other game engines) is a simulation of light in the real world. Even if you’re working on a fantastical project that doesn’t follow the laws of physics, that simulation of light as we know and experience it can help ground your game or other real-time experience and make it feel more real.

All light needs a source — something that emits it, like the sun or a light bulb. Light is energy that travels from that source in straight lines in the form of waves. 

There are three key properties of that source that impact the light:
- Its shape will determine the direction in which the light waves are emitted.
- Its size will determine the area that the light impacts.
- Its strength (or intensity) will determine how far those light waves can travel and how bright it is.
Consider these three properties for a flashlight. The light bulb that emits light is small (size) and circular (shape), but it is strong enough to light that small area brightly (intensity).

For someone or something to perceive light, two things are required:
- A light source, which emits light, like a light bulb or the sun.
- A light sensor to receive it, like the retina in your eye or the image sensor in a digital camera.
When you see an object, the information that you are receiving is light waves bouncing off that object and hitting your light sensor — your eye’s retina.

![](https://unity-connect-prd.storage.googleapis.com/20211122/learn/images/3a324a58-24d3-4599-ae6b-e6699d0d909e_CC_Light_Graphic_3.png)

This is the process called reflection. There are two kinds of reflection:
- When light waves hit a very smooth surface and create a mirror image.
- When light waves hit a non-smooth surface, some energy is absorbed and the rest is reflected back in all sorts of different directions.


- Reflection: When a light wave impacts a surface and is redirected, as you learned in the previous step.
- Refraction: When a light wave passes through something other than air (like water or glass) and its path is changed by that.

Before you get started with lighting in Unity, there’s one more underlying concept that you need to know: the difference between direct and indirect light. This will enable you to light scenes effectively and understand the role of the different lighting systems in Unity.

Direct light is light that is emitted, hits a surface once, and then is reflected directly into a sensor. 

![](https://unity-connect-prd.storage.googleapis.com/20211123/learn/images/8b8c4edf-99f2-4a9d-ba43-6881e974322b_CC_Light_Graphic_4.png)

Indirect light is all the other light that ends up reflected into a sensor, like light that hits surfaces several times and light from the sky when you’re not looking at the sun directly. (Remember, the sun is a strong light source, so it’s very dangerous to do that!) 

![](https://unity-connect-prd.storage.googleapis.com/20211123/learn/images/95d6d23b-4593-44d5-b33b-40e20cbacbb1_CC_Light_Graphic_5.png)

## procedural skybox

1. In the Project window, navigate to Assets > CreativeCore_Lighting > Materials
2. Right-click in the window and select Create > Material. Give your new material a clear name, to help you find it later.
3.  In the Inspector, go to the Shader property and select Skybox > Procedural using the dropdown.  

In material tab,
- Sun: This is the method that Unity uses to create a sun disk in the skybox. Set this to Simple.
- Sun Size: This is the size modifier for the sun disk — the higher the value, the larger it will appear in the sky. 
- Atmosphere Thickness: The density of the atmosphere — the more dense an atmosphere, the more light will be absorbed by it.
- Sky Tint: A color tint for the sky.
- Ground: The color of the area below the horizon (the ground).
- Exposure: This adjusts the sky’s exposure. Larger values produce a more exposed skybox that seems brighter.

Let’s say that we wanted to develop this example to create a more realistic-feeling night look. We could try adjusting the colors and slightly decreasing the Atmospheric Thickness value in the procedural skybox material: 
![](https://unity-connect-prd.storage.googleapis.com/20211123/learn/images/203499f7-9794-422c-ac22-cb1537da6e83_CC_Light_3.8.0_2_NightSkyExample2Update.png)

## types of light source

- Point Lights: These lights send out light in all directions equally from a point in space. You can use them to simulate light sources like lamps. They are represented in the Scene view with a light bulb icon.

- Spot Lights: These lights send out light in a cone-shape from a point in space. You can use them to simulate light sources like flashlights. They are represented in the Scene view with an icon that looks a bit like a spotlight.

 In the Light component, find the Type property and change it to Point using the dropdown. Notice the difference this makes to the shape of the light cast by the street lamp: the light it emits is now being sent out in all directions equally, rather than constrained by the cone shape of a Spot Light. 
 

The Range of a Spot Light is capped due to the limitations of its shape. 

Drag right or left on the Intensity property to increase or decrease the strength of the light within its set range. As with Range, you can also manually input a value.

In the real world, there’s an inverse relationship between how far away from a light source you are and the intensity of the light emitted. For example, imagine that you are walking in the dark with a flashlight. The area within the flashlight's beam will be brightly illuminated. The further away from the beam you move, the lower the strength of the light and the weaker the illumination.

3.  Try setting a very high Intensity value — over 1500. You can take the intensity of a light beyond a natural intensity for the source and range in Unity, though for motivated lighting you should use this with care. In this case, setting the Intensity property too high makes the street lamp look more like a floodlight than an actual street lamp! 

 The Indirect Multiplier property impacts the intensity of the indirect light provided by this light source (light that bounces multiple times before being received by a sensor). If you set it:

Below 1, the indirect light will be dimmer each time it bounces off an object. This is the way real light behaves, but you might want to override that behavior to achieve a particular lighting effect.

Above 1, the indirect light will become brighter with each bounce. This is not natural, but it can be very useful if you’re trying to illuminate a dark, enclosed space in your scene.
For now, leave this set to 1.

In an interactive experience, there are normally at least some dynamic elements at play. These might be props, vehicles or characters — they’ll all be illuminated by your lighting too.

### Light Probe

You can use Light Probes to make your baked lighting much more realistic. They are also relatively efficient to use at runtime compared to real-time lights, if you place them with care. 
Although Light Probes are generally useful to address issues with baked lighting that you might encounter when lighting dynamic objects, they are also very useful for areas in a scene where there are significant changes in the lighting. If users don’t see dynamic objects respond to lighting in the way that they expect in these areas, it can negatively impact their immersion in an experience.

Skyboxes do not contribute to direct lighting in a scene.