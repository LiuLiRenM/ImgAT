# ImgAT
ImageAnalyzeTool（图片分析工具）
# 工作流设计
- 读取图片，获取长宽等信息，写入数据库（批量写）
- 上传图片到OBS（单个图片）
- 调用image-nsfw-detector-service服务（单个图片）
- 更新结果（单个图片）
- 删除上传到OBS的图片和结果文件（单个图片）