const request = await fetch("cvj.stl");
const stl = await request.arrayBuffer();
const magicChunk = stl.slice(0, 5);
const textDecoder = new TextDecoder("ascii");
const isBinarySTL = textDecoder.decode(magicChunk) == "solid";