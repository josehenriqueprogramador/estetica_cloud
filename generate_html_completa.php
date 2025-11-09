<?php
$baseDir = __DIR__; // raiz do projeto

function listFilesAllLevels($dir) {
    $result = [];
    $items = scandir($dir);
    foreach ($items as $item) {
        if ($item === '.' || $item === '..') continue;
        if (strpos($item, '.pyc') !== false || $item === 'estrutura_completa.html' || $item === 'generate_html_completa.php' || $item === '__pycache__') continue;

        $path = $dir . DIRECTORY_SEPARATOR . $item;
        if (is_dir($path)) {
            $result[$item] = listFilesAllLevels($path);
        } else {
            $result[] = $path;
        }
    }
    return $result;
}

function generateHTMLTree($files, $level = 0) {
    $html = "<ul style='list-style:none;padding-left:" . ($level * 20) . "px;'>";
    foreach ($files as $key => $value) {
        if (is_array($value)) {
            $html .= "<li><span class='folder' onclick='toggleFolder(this)'>📁 " . htmlspecialchars($key) . "</span>";
            $html .= generateHTMLTree($value, $level + 1);
            $html .= "</li>";
        } else {
            $filename = basename($value);
            $content = htmlspecialchars(file_get_contents($value));
            $html .= "<li><span class='file' onclick='toggleFile(this)'>📄 $filename</span>";
            $html .= "<pre class='file-content' style='display:none; margin-top:5px;'>$content</pre>";
            $html .= "</li>";
        }
    }
    $html .= "</ul>";
    return $html;
}

$structure = listFilesAllLevels($baseDir);
$html = "<!DOCTYPE html>
<html lang='pt-br'>
<head>
<meta charset='UTF-8'>
<title>Estrutura Completa do Projeto</title>
<style>
body { font-family: Arial, sans-serif; padding: 20px; background: #fefefe; color: #333; }
ul { margin:0; padding:0; }
li { margin:2px 0; }
.folder { cursor: pointer; font-weight: bold; color: #007bff; }
.file { cursor: pointer; color: #555; }
pre { background:#f4f4f4; padding:10px; border:1px solid #ccc; overflow:auto; border-radius:4px; }
</style>
</head>
<body>
<h1>📂 Estrutura Completa do Projeto</h1>
<p>Clique nas pastas ou arquivos para expandir/contrair.</p>
" . generateHTMLTree($structure) . "
<script>
function toggleFolder(el) {
    let next = el.nextElementSibling;
    if (!next) return;
    next.style.display = (next.style.display === 'none' || next.style.display === '') ? 'block' : 'none';
}
function toggleFile(el) {
    let next = el.nextElementSibling;
    if (!next) return;
    next.style.display = (next.style.display === 'none' || next.style.display === '') ? 'block' : 'none';
}
</script>
</body>
</html>";

file_put_contents('estrutura_completa.html', $html);
echo "✅ HTML completo gerado com sucesso em 'estrutura_completa.html'!\n";
