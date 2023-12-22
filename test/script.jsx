var proj = app.project

// 새로운 컴포지션 생성
var comp = proj.items.addComp("MyComposition", 1920, 1080, 1.0, 10, 30);

// 텍스트 레이어 추가
var textLayer = comp.layers.addText("Hello, After Effects!");
textLayer.position.setValue([comp.width / 2, comp.height / 2]);

// 스크립트 실행 후 저장
proj.save("test_project.aep");