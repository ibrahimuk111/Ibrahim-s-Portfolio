// Author: Muhammad Ibrahim
// Email: ukibrahim111@gmail.com
// Flutter Mobile App with On-Device AI Integration

import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ExecuTorch AI Mobile',
      theme: ThemeData(primarySwatch: Colors.deepPurple),
      home: const HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('ExecuTorch AI Flutter')),
      body: const Center(child: Text('On-Device AI Engine Active')),
    );
  }
}
