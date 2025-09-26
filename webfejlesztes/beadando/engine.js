async function parseSTL() {
  const request = await fetch("cvj.stl");
  const stl = await request.arrayBuffer();

  const magicChunk = stl.slice(0, 5);
  const textDecoder = new TextDecoder("ascii");
  const header = textDecoder.decode(magicChunk);
  const isAsciiSTL = header === "solid";
  const triangleCount = dv.getUint32(0, true);
  const dv = new DataView(stl, 80);
  if (!isAsciiSTL) {
    console.log("Binary STL, triangles:", triangleCount);
  } else {
    console.log("ASCII STL");
  }

  const triangles = [];
  for (let i = 0; i < triangleCount; i++) {
    // 2 bytes triangle count + 50 bytes per triangle
    const triangleOffset = 4 + 50 * i;
    const triangle = [
      {
        x: dv.getFloat32(triangleOffset + 4 * 4, true),
        y: dv.getFloat32(triangleOffset + 5 * 4, true),
        z: dv.getFloat32(triangleOffset + 6 * 4, true),
      },
      {
        x: dv.getFloat32(triangleOffset + 7 * 4, true),
        z: dv.getFloat32(triangleOffset + 8 * 4, true),
        y: dv.getFloat32(triangleOffset + 9 * 4, true),
      },
      {
        x: dv.getFloat32(triangleOffset + 10 * 4, true),
        z: dv.getFloat32(triangleOffset + 11 * 4, true),
        y: dv.getFloat32(triangleOffset + 12 * 4, true),
      },
    ];
    triangles.push(triangle);
  }
  const canvas = document.querySelector("#js-stl-render-output");
  canvas.width = canvas.offsetWidth;
  canvas.height = canvas.offsetHeight;
  const ctx = canvas.getContext("2d");

  const flattenedTriangles = triangles.flat();
  const minX = Math.min(...flattenedTriangles.map((p) => p.x));
  const maxX = Math.max(...flattenedTriangles.map((p) => p.x));
  const minY = Math.min(...flattenedTriangles.map((p) => p.y));
  const maxY = Math.max(...flattenedTriangles.map((p) => p.y));

  // make the model perfectly fill the canvas
  const maxScaleX = canvas.width / (maxX - minX);
  const maxScaleY = canvas.height / (maxY - minY);
  const scale = Math.min(maxScaleX, maxScaleY);

  // shift the model to be perfectly centered
  const center = {
    x: canvas.width / 2,
    y: canvas.height / 2,
  };
  const shift = {
    x: center.x - ((maxX + minX) / 2) * scale,
    y: center.y - ((maxY + minY) / 2) * scale,
  };
  ctx.strokeStyle = "#fff";
  ctx.fillStyle = "#aaa";
  for (const triangle of triangles) {
    ctx.beginPath();
    ctx.moveTo(
      shift.x + triangle[0].x * scale,
      shift.y + triangle[0].y * scale
    );
    ctx.lineTo(
      shift.x + triangle[1].x * scale,
      shift.y + triangle[1].y * scale
    );
    ctx.lineTo(
      shift.x + triangle[2].x * scale,
      shift.y + triangle[2].y * scale
    );
    ctx.closePath();
    ctx.stroke();
    ctx.fill();
  }
}
parseSTL();
