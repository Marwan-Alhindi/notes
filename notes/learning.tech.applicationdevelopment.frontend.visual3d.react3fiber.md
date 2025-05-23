---
id: bd3r4sep9stkixaw7xsympb
title: React3fiber
desc: ''
updated: 1747860594605
created: 1747655657221
---


1.	Core Concepts
2.	Scene Setup
3.	Geometries & Materials
4.	Lights & Shadows
5.	Camera & Controls
6.	Animations
7.	Loading Models (GLTF, OBJ)
8.	Interactions & Events
9.	Performance Optimization
10.	Integration with Drei & Other Tools


- What are the parts of R3F, the general components or R3F and you can refer to it from the documentation?
- Whats the main word about react and react three fiber that explain it? re...
- Whats a mesh and how to create one?
- What every mesh should have?
- How to create a geometry and a material for the mesh?
- How to control the position and the rotation of the mesh?
- Whats a canvas/scene and how to create one?
- How to group components in R3F?
- How do you use tailwind with react? give me an example of how to resize the canvas in tailwind?
- How do you give redefine the parameters for the components?
- What are the main things that you can do to shapes? i.e scale and...?
- How to animate? Whats useFrame? and how to use it? 
- Whats a reference? and how to use it?
- Every computer render frames in different speed and so the animation will be different.. how do you make it responsive to all devices? 
- For threejs components like OrbitControls, how to use it inside react? What about drei?

# Camera, Rotation & Position
- Where does the camera always look at by default?
- When you change the position of the camera, what happens to the objects coordinate system when you rotate them?
- Where does the light looks at?



 # Lesson 1:
 - useRef
 - useFrame
 - mesh: geometry + material
   - position
   - rotation
   - scale
 - camera
   - position
 - group
 - extend
 - OrbitControls
 - useThree
 - directional light
 - ambient light
 - CustomObjects
 - Float32Array
 - Triangles, vertices and three values per vertex
 - buffer geometry, buffer attribute, attaching buffer attribute to geometry
   - attributes-position == geometry attribute.position.
   - count, itemsSize and array positions
 - DoubleSide to material
 - useMemo 
 - difference between useMemo and useState
 - computeVertexNormals (you must use it with useEffect)
 - useEffect
 - Canvas camera
   - fov,near, far and positions, zoom
 - Canvas orthographic
 - Animating Canvas camera (rotating)
   - state.clock.elapsedTime (from useFrame)
   - Trigonometry to rotate the camera 
   - camera.lookAt(0,0,0)
 - Canvas antialias
 - toneMapping
   - Canvas flat color
   - CineonToneMapping
   - ACESFilmicToneMapping
 - outputEncoding or (outputColorSpace)
   - LinearEncoding
   - sRGBEncoding
 - background color (from css)
 - Pixel Ratio
   - dpr

# Lesson 2
- Drei
- https://drei.docs.pmnd.rs/getting-started/introduction

## Controls
- Orbitcontrols, damping and makeDefault
- TransformControls
  - Center of a mesh instead of center of the scene - two solutions: reference and positioning
  - Translate, scale and rotate
- Fixing the conflit of OrbitControl and TransformControls
- PivotControls (for users to control things)
  - anchor, depthTest
  - lineWidth
  - axisColors
  - scale
  - perspective (fixed attribute)
  - How to put it inside the object


## Html inside the website!
- Whats the difference between html and text§
- how to add style
  - position
  - wrapperClass
  - center
  - distanceFactor
  - useRef to disappear the text when blocked by other blocks
- how to add buttons and p..etc

## Texts!!
- Text
  - font
  - woff is the lighter format
  - fontSize
  - color
  - material
  - position,rotation and scale
  - maxWidth
  - converting font:
    - https://transfonter.org/
    - https://www.fontsquirrel.com/tools/webfont-generator

## Minimum distance between a point and a shape
- SDF
  -  https://iquilezles.org/articles/distfunctions2d/
  -  https://iquilezles.org/articles/distfunctions/
- Since you cant express text mathematically, whats the approach used to have characters?

## Float
- Float on all objects!
  - speed
  - floatIntensity

## MeshReflectorMaterial
- resolution
- blur
- mixBlur
- mirror
- color
- 