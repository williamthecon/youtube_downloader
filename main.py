from pytube import YouTube

def download(link, no_print=False, choose_version=True, best_video=False, best_audio=False, path="", file_name=None, file_type="mp4", return_yt=True, return_stream=True, return_file_path=True):
	try:
		yt = YouTube(link)
	except Exception as error:
		print(f"Can't load this link: {error}") if not no_print else None
		return None
	
	if best_video:
		pass
	elif best_audio:
		stream = yt.streams.filter(mime_type="audio/mp4", abr="128kbps")[0]	
	elif choose_version:
		pass
	else:
		print("Don't no which version to download") if not no_print else None
		return None
		
	if file_name is None:
		file_name = yt.title
		
	stream.download(path, f"{file_name}.{file_type}")
	
	returns = []
	if return_yt:
		returns.append(yt)
	if return_stream:
		returns.append(stream)
	if return_file_path:
		returns.append(f"{path}/{file_name}.{file_type")
	
	return returns

