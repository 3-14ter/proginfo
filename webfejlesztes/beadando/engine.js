async function checkSTL() {
  const response = await fetch("cvj.stl");
  const buffer = await response.arrayBuffer();

  // Take first 80 bytes (header)
  const header = buffer.slice(0, 80);

  const decoder = new TextDecoder("ascii");
  const headerText = decoder.decode(header).trim();

  const isAscii = headerText.startsWith("solid");

  console.log("Header:", headerText.substring(0, 20));
  console.log("Likely ASCII STL?", isAscii);
}

checkSTL();
