#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-astrolabe
Version  : 1.3.1
Release  : 4
URL      : https://rubygems.org/downloads/astrolabe-1.3.1.gem
Source0  : https://rubygems.org/downloads/astrolabe-1.3.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-fuubar
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rubygems-tasks

%description
[![Gem Version](http://img.shields.io/gem/v/astrolabe.svg)](http://badge.fury.io/rb/astrolabe)
[![Dependency Status](http://img.shields.io/gemnasium/yujinakayama/astrolabe.svg)](https://gemnasium.com/yujinakayama/astrolabe)
[![Build Status](https://travis-ci.org/yujinakayama/astrolabe.svg?branch=master)](https://travis-ci.org/yujinakayama/astrolabe)
[![Coverage Status](http://img.shields.io/coveralls/yujinakayama/astrolabe/master.svg)](https://coveralls.io/r/yujinakayama/astrolabe)
[![Code Climate](http://img.shields.io/codeclimate/github/yujinakayama/astrolabe.svg)](https://codeclimate.com/github/yujinakayama/astrolabe)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n astrolabe-1.3.1
gem spec %{SOURCE0} -l --ruby > rubygem-astrolabe.gemspec

%build
gem build rubygem-astrolabe.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
astrolabe-1.3.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/astrolabe-1.3.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/.rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/Guardfile
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/astrolabe.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/benchmark/.rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/benchmark/benchmark_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/benchmark/performance_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/lib/astrolabe.rb
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/lib/astrolabe/builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/lib/astrolabe/node.rb
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/lib/astrolabe/sexp.rb
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/lib/astrolabe/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/spec/.rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/spec/astrolabe/node_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/spec/astrolabe/sexp_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/astrolabe-1.3.1/spec/support/shared_contexts.rb
/usr/lib64/ruby/gems/2.3.0/specifications/astrolabe-1.3.1.gemspec
