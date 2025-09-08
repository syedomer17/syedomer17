# 🐍 GitHub Snake Contribution Graph

This repository includes an automated GitHub snake game that visualizes contribution activity in a fun, animated way!

## 🎮 Features

- **Multiple Themes**: Classic, Ocean, Retro, Neon, Matrix styles
- **Responsive Design**: Light/dark mode support
- **Automated Updates**: Runs daily at midnight UTC
- **Interactive Elements**: Hover effects and expandable sections
- **Multiple Formats**: SVG and GIF animations

## 🛠️ How It Works

The snake is generated using the [Platane/snk](https://github.com/Platane/snk) action which:

1. **Fetches contribution data** from your GitHub profile
2. **Generates animations** showing a snake eating your contributions
3. **Creates multiple themed versions** with different color schemes
4. **Deploys to output branch** for use in README

## 🎨 Available Themes

| Theme | Description | Format |
|-------|-------------|---------|
| Classic | Standard GitHub colors with light/dark mode | SVG |
| Ocean | Blue ocean-inspired gradient | GIF |
| Retro | Green terminal/console style | SVG |
| Neon | Cyberpunk pink/purple theme | SVG |
| Matrix | Digital rain green theme | SVG |
| Rainbow | Multicolor animated matrix | GIF |
| Matrix Animated | Green matrix with animation | GIF |

## 🔧 Customization

You can customize the snake by modifying the workflow file `.github/workflows/snake.yml`:

```yaml
outputs: |
  dist/custom-snake.svg?color_snake=#your_color&color_dots=#color1,#color2,#color3,#color4,#color5
```

### Color Parameters:
- `color_snake`: The snake's color
- `color_dots`: Contribution level colors (least to most active)

## 📦 Manual Trigger

You can manually trigger the snake generation:
1. Go to the **Actions** tab
2. Select **Generate GitHub Snake Animations**
3. Click **Run workflow**

## 🚀 Installation for Your Profile

To add this to your own GitHub profile:

1. Copy the `.github/workflows/snake.yml` file
2. Add the snake section to your README.md
3. Update the image URLs to point to your repository
4. Commit and push to trigger the first generation

## 📊 File Sizes

- SVG files: ~105KB each
- GIF files: ~350KB each
- Total storage: ~2MB for all variations

## 🔄 Update Schedule

- **Automatic**: Daily at 00:00 UTC
- **Manual**: Via workflow dispatch
- **On Push**: When main branch is updated

---

*Generated with ❤️ using GitHub Actions and the amazing Platane/snk project*