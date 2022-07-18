1. Get publish profile from hosting
2. dotnet publish /p:PublishProfile=[file from hosting:site1.PublishSettings]
3. cd bin/Debug/net6.0/publish
4. 7z a [archiveName].zip .
5. Deploy all files in hosting
6. Add errors in Web.config
