class WashingtonFootball < Formula
  include Language::Python::Virtualenv

  desc "Shiny new formula"
  homepage "https://github.com/kmcquade/washington_football"
  url "https://files.pythonhosted.org/packages/d9/fa/337ad4b6809f49de41a36ab625af1d273c4d73f29b0b3d6704aa2a4727bc/washington_football-0.0.3.5.tar.gz"
  sha256 "451f7e2294eb45bf27cb64252b669c2b729e1de515787d0e9cd3a5474ff04628"

  depends_on "python3"

  resource "click" do
    url "https://files.pythonhosted.org/packages/27/6f/be940c8b1f1d69daceeb0032fee6c34d7bd70e3e649ccac0951500b4720e/click-7.1.2.tar.gz"
    sha256 "d2b5255c7c6349bc1bd1e59e08cd12acbbd63ce649f2588755783aa94dfb6b1a"
  end

  def install
    virtualenv_create(libexec, "python3")
    virtualenv_install_with_resources
  end

  test do
    false
  end
end
