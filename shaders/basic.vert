#version 400

layout(location=0) in vec3 position;
layout(location=1) in vec3 color;

out vec3 oColor;

void main(){
    oColor = color;
    gl_Position = vec4(position, 1.0);
}