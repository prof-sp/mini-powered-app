import 'package:flutter/material.dart';
import 'dart:io';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override Widget build(BuildContext ctx) {
    return MaterialApp(home: HomePage());
  }
}

class HomePage extends StatefulWidget {
  @override _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage>{
  File? _image;
  String _result = "";

  Future pickAndUpload() async {
    final picker = ImagePicker();
    final picked = await picker.pickImage(source: ImageSource.camera, maxWidth: 800);
    if(picked == null) return;
    setState(() => _image = File(picked.path));

    var uri = Uri.parse("http://your-backend-host:8000/inspect");
    var request = http.MultipartRequest('POST', uri);
    request.files.add(await http.MultipartFile.fromPath('file', _image!.path));
    var resp = await request.send();
    var body = await resp.stream.bytesToString();
    setState(() => _result = body);
  }

  @override Widget build(BuildContext ctx){
    return Scaffold(
      appBar: AppBar(title: Text("AFQSM Mobile")),
      body: Center(
        child: Column(mainAxisSize: MainAxisSize.min, children: [
          _image != null ? Image.file(_image!, height: 250) : Icon(Icons.camera_alt, size:120),
          SizedBox(height:12),
          ElevatedButton(onPressed: pickAndUpload, child: Text("Scan & Upload")),
          SizedBox(height:12),
          Text(_result, style: TextStyle(fontSize:12)),
        ]),
      ),
    );
  }
}
