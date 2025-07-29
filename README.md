# Steel Heat Treatment Assistant

A comprehensive Python GUI application for calculating iron smelting and heat treatment parameters. This tool helps engineers and metallurgists determine optimal heating times, cooling rates, and temperature profiles for steel heat treatment processes.

## Features

### Core Functionality
- **Shape-based Face Calculations**: Add and edit geometric faces (Circle, Rectangle, Triangle, Square, Ellipse, Hexagon)
- **Carbon Percentage Analysis**: Input carbon content (0-2%) for temperature calculations
- **Process Parameter Selection**: Configure K1, K2, K3 parameters for different heating conditions
- **Advanced Cooling Options**: Multiple cooling parameter selection methods

### Cooling Parameter Options
1. **تبريد داخل الفرن (تخمير كامل)** - Custom cooling value input
2. **تبريد بالماء** - Water cooling with predefined options
3. **تبريد بالزيت** - Oil cooling (automatic selection)

### Calculations
- **Minimum Distance**: Calculated from the face with maximum area
- **Temperature Calculation**: Based on carbon percentage using linear interpolation
- **Heating Time (Th)**: Th = 0.1 × D × K1 × K2 × K3
- **Keeping Time**: Equal to minimum distance
- **Cooling Time (Tc)**: Tc = (T* - 25) / C

### Visualization
- **Temperature Profile Chart**: Interactive matplotlib chart showing the complete heat treatment cycle
- **Results Report**: Detailed calculation summary with all parameters

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd metal_smelting_assistant
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## Usage Guide

### Adding Faces
1. Click "Add Face" button
2. Select a shape from the popup window
3. Enter the required dimensions (radius, width/height, etc.)
4. Click "Submit" to add the face

### Editing Faces
- Click the "Edit" button next to any face to modify its parameters
- Click "Delete" to remove unwanted faces

### Setting Parameters
1. **Carbon Percentage**: Enter a value between 0-2%
2. **K1 Parameter**: Choose heating medium
   - حوض المعدن المنصهر (0.5)
   - حوض أملاح منصهرة (1.0)
   - وسط غازي (2.0)

3. **K2 Parameter**: Choose shape factor
   - كرة (1.0)
   - المحور والمقطع الدائري (2.0)
   - المحور على شكل متوازي مستطيلات (2.5)
   - صفيحة (4.0)

4. **K3 Parameter**: Choose heating method
   - تسخين من جميع الجهات (1.0)
   - تسخين من ثلاث جهات (1.5)
   - تسخين من جهة واحدة (4.0)

5. **Cooling Parameter**: Choose cooling method
   - اختر معامل التبريد (default)
   - تبريد داخل الفرن (تخمير كامل) - Custom value input
   - تبريد بالماء - Water cooling options
   - تبريد بالزيت - Oil cooling (250)

### Getting Results
1. Ensure at least one face is added
2. Fill in all required parameters
3. Click "Submit" to view results
4. Review the calculation report and temperature chart

## Technical Details

### Temperature Calculation
The application uses linear interpolation between known temperature-carbon percentage points:

- **For carbon > 0.8%**: Linear interpolation between (0.8, 723°C) and (2.0, 1147°C)
- **For carbon ≤ 0.8%**: Linear interpolation between (0.0, 910°C) and (0.8, 723°C)

### Area Calculations
- **Circle**: π × radius²
- **Rectangle**: width × height
- **Triangle**: 0.5 × base × height
- **Square**: side²
- **Ellipse**: π × major_axis × minor_axis / 4
- **Hexagon**: (3√3/2) × side_length²

## File Structure
```
metal_smelting_assistant/
├── main.py              # Main application file
├── requirements.txt      # Python dependencies
├── README.md           # This file
└── prompt.txt          # Development notes
```

## Dependencies

The application requires the following Python packages:
- `tkinter` - GUI framework (included with Python)
- `matplotlib` - Chart creation and visualization
- `math` - Mathematical calculations (built-in)

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.7 or higher
- **Memory**: Minimum 512MB RAM
- **Display**: 1024x768 or higher resolution

## Troubleshooting

### Common Issues

1. **Import Error for matplotlib**
   ```bash
   pip install matplotlib
   ```

2. **GUI not displaying properly**
   - Ensure your system supports tkinter
   - Try running on a different display resolution

3. **Calculation errors**
   - Verify all input values are positive numbers
   - Check that carbon percentage is between 0-2%

### Getting Help

If you encounter issues:
1. Check that all dependencies are installed correctly
2. Verify Python version compatibility
3. Review the console output for error messages

## Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Version History

- **v1.0.0**: Initial release with basic functionality
- **v1.1.0**: Added cooling parameter options and temperature chart
- **v1.2.0**: Enhanced UI with Arabic labels and improved validation

---

**Note**: This application is designed for educational and professional use in metallurgy and materials science. Always verify calculations with standard engineering practices and consult with qualified professionals for critical applications.
